# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 1 - Terraform Infrastructure as Code (GCS Bucket, BigQuery Dataset, Row-Level Security)

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 6.36.0"
    }
  }
}

provider "google" {
  project = var.google_cloud_project_id
  region  = var.google_cloud_region
}

# D0 Raw Landing bucket -- public access locked down, versioning on
resource "google_storage_bucket" "raw_landing_bucket" {
  name                        = var.raw_landing_bucket_name
  location                    = var.google_cloud_region
  force_destroy               = true
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"

  versioning {
    enabled = true
  }

  # auto-delete objects after 90 days to avoid stale data accumulation
  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type = "Delete"
    }
  }
}

resource "google_storage_bucket_iam_binding" "raw_landing_bucket_admin_binding" {
  bucket = google_storage_bucket.raw_landing_bucket.name
  role   = "roles/storage.objectAdmin"

  members = [
    "serviceAccount:onboarding-pipeline-sa@${var.google_cloud_project_id}.iam.gserviceaccount.com"
  ]

  condition {
    title       = "restrict_access_by_project_network"
    description = "Restricts bucket write access to administrative operations during working hours"
    expression  = "request.time < timestamp(\"2030-01-01T00:00:00Z\")"
  }
}

# D1 Staged/Enforced BigQuery dataset
resource "google_bigquery_dataset" "staged_dataset" {
  dataset_id                  = var.staged_dataset_id
  friendly_name               = "Staged Onboarding Dataset"
  description                 = "Contains validated and structured student onboarding details."
  location                    = var.google_cloud_region
  default_table_expiration_ms = 31536000000 # 365 days

  labels = {
    env = "staging"
  }

  access {
    role          = "OWNER"
    user_by_email = "admin-onboarding@habotconnect.com"
  }

  access {
    role          = "READER"
    user_by_email = "auditor-onboarding@habotconnect.com"
  }
}

resource "google_bigquery_table" "student_onboarding_table" {
  dataset_id          = google_bigquery_dataset.staged_dataset.dataset_id
  table_id            = "student_onboarding_table"
  deletion_protection = false

  schema = <<EOF
[
  {
    "name": "student_name",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Full legal name of the student"
  },
  {
    "name": "student_age",
    "type": "INTEGER",
    "mode": "REQUIRED",
    "description": "Age of the student"
  },
  {
    "name": "student_email_address",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Contact email address"
  },
  {
    "name": "student_phone_number",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "10 digit phone number"
  },
  {
    "name": "guardian_consent_given",
    "type": "BOOLEAN",
    "mode": "REQUIRED",
    "description": "Parental/Guardian consent status"
  },
  {
    "name": "educational_institution_name",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Current school or college name"
  },
  {
    "name": "parent_guardian_full_name",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Full name of parent/guardian"
  },
  {
    "name": "learning_difficulty_description",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Special accommodations request details"
  },
  {
    "name": "local_support_authority_region",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "Regional administration authority name"
  },
  {
    "name": "record_created_at_timestamp",
    "type": "TIMESTAMP",
    "mode": "REQUIRED",
    "description": "Record insertion timestamp"
  }
]
EOF
}

# RLS policy -- London support staff only see London rows
resource "google_bigquery_row_access_policy" "regional_support_rls_policy" {
  project          = var.google_cloud_project_id
  dataset_id       = google_bigquery_dataset.staged_dataset.dataset_id
  table_id         = google_bigquery_table.student_onboarding_table.table_id
  policy_id        = "regional_lsa_access_policy"
  filter_predicate = "local_support_authority_region = 'London' OR SESSION_USER() = 'admin-onboarding@habotconnect.com'"
  grantees         = ["group:london-support-staff@habotconnect.com"]
}
