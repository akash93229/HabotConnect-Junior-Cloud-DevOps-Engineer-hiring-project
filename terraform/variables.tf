# Project Name: HabotConnect Project
# Task Name: Terraform Infrastructure Input Variables
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

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
