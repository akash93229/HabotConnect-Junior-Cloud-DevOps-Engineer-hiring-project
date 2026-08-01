# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 1 - Terraform Input Variable Definitions

variable "google_cloud_project_id" {
  type    = string
  default = "habotconnect-staging-project"
}

variable "google_cloud_region" {
  type    = string
  default = "europe-west2"
}

variable "raw_landing_bucket_name" {
  type    = string
  default = "habotconnect-d0-raw-landing-bucket"
}

variable "staged_dataset_id" {
  type    = string
  default = "d1_staged_enforced"
}
