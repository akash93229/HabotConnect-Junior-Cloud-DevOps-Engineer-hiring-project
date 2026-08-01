# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 1 - Terraform Infrastructure Output Values

output "raw_landing_bucket_url" {
  value = google_storage_bucket.raw_landing_bucket.url
}

output "raw_landing_bucket_name" {
  value = google_storage_bucket.raw_landing_bucket.name
}

output "staged_dataset_id" {
  value = google_bigquery_dataset.staged_dataset.dataset_id
}

output "staged_dataset_unique_id" {
  value = google_bigquery_dataset.staged_dataset.id
}

output "onboarding_table_id" {
  value = google_bigquery_table.student_onboarding_table.id
}

output "row_level_security_policy_id" {
  value = google_bigquery_row_access_policy.regional_support_rls_policy.id
}
