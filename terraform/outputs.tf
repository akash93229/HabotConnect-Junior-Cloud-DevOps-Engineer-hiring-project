# Project Name: HabotConnect Project
# Task Name: Terraform Infrastructure Outputs
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

output "raw_landing_bucket_url" {
  value       = google_storage_bucket.raw_landing_bucket.url
  description = "The direct URL scheme pointing to the provisioned Google Cloud Storage bucket (D0 Raw Landing)."
}

output "raw_landing_bucket_name" {
  value       = google_storage_bucket.raw_landing_bucket.name
  description = "The exact name of the provisioned Google Cloud Storage bucket."
}

output "staged_dataset_id" {
  value       = google_bigquery_dataset.staged_dataset.dataset_id
  description = "The dataset identifier for the BigQuery dataset (D1 Staged/Enforced)."
}

output "staged_dataset_unique_id" {
  value       = google_bigquery_dataset.staged_dataset.id
  description = "The unique resource identifier for the BigQuery dataset (D1 Staged/Enforced)."
}

output "onboarding_table_id" {
  value       = google_bigquery_table.student_onboarding_table.id
  description = "The unique resource identifier for the student onboarding BigQuery table."
}

output "row_level_security_policy_id" {
  value       = google_bigquery_row_access_policy.regional_support_rls_policy.id
  description = "The identifier of the applied BigQuery Row-Level Security policy."
}
