# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 1 - Terraform Cloud Shell Execution Proof

variable "google_cloud_project_id" {
  type        = string
  description = "The Google Cloud Platform project identifier where resources will be provisioned."
  default     = "habotconnect-staging-project"
}

variable "google_cloud_region" {
  type        = string
  description = "The geographic region where regional Google Cloud resources will be deployed."
  default     = "europe-west2"
}

variable "raw_landing_bucket_name" {
  type        = string
  description = "The globally unique name for the Google Cloud Storage bucket (D0 Raw Landing)."
  default     = "habotconnect-d0-raw-landing-bucket"
}

variable "staged_dataset_id" {
  type        = string
  description = "The identifier for the BigQuery dataset (D1 Staged/Enforced)."
  default     = "d1_staged_enforced"
}
