# Project Name: HabotConnect Project
# Task Name: Terraform Infrastructure Input Variables
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

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
