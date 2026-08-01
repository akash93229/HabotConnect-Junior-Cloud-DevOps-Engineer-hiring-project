# Project Name: HabotConnect Project
# Task Name: Project Documentation README
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

# HabotConnect Project

This repository contains the deliverables for the HabotConnect FZCO hiring assessment for the **Junior Cloud & DevOps Engineer (GCP / Django / React)** position. 

The project addresses a simulated staging environment incident where credentials were leaked and database schemas were mismatched. It implements a robust, secure, and automated solution across three key areas: Infrastructure as Code, CI/CD safety gates, and strict backend input validation.

---

## Folder Structure

The repository is structured as follows:

```
HabotConnect_Project/
├── .gitignore                       # Git exclusion rules configuration
├── README.md                        # Project documentation (this file)
├── django/                          # Django Backend Application
│   ├── core/                        # Django Project Settings and Routing
│   │   ├── __init__.py
│   │   ├── settings.py              # Configuration including DRF and Student App
│   │   ├── urls.py                  # API router mapping for endpoints
│   │   ├── wsgi.py                  # WSGI Gateway configuration
│   │   └── asgi.py                  # ASGI Gateway configuration
│   ├── student/                     # Onboarding Application App
│   │   ├── __init__.py
│   │   ├── apps.py                  # App configuration details
│   │   ├── models.py                # StudentOnboarding database model
│   │   ├── serializers.py           # StudentOnboardingSerializer with DCYN logic
│   │   ├── views.py                 # StudentOnboardingCreateView endpoint handler
│   │   └── urls.py                  # Local endpoint routing
│   ├── manage.py                    # Django administrative command-line utility
│   ├── models.py                    # Wrapper forwarding imports to student.models
│   ├── serializers.py               # Wrapper forwarding imports to student.serializers
│   └── views.py                     # Wrapper forwarding imports to student.views
├── docs/                            # Project architectural artifacts
│   └── architecture.png             # Modern system design and workflow visualization
├── pipeline/                        # CI/CD Workflows
│   └── github-actions.yml           # Poka-Yoke "Fail-Closed" GitHub Actions Pipeline
├── sample-data/                     # Development sample data
│   └── student.json                 # Test payloads (Valid, Invalid Age, Missing Consent)
└── terraform/                       # Infrastructure as Code
    ├── main.tf                      # Resource definitions for GCS, BigQuery, and RLS
    ├── variables.tf                 # Variable declarations for project/region configs
    └── outputs.tf                   # Outputs for resource names and resource URLs
```

---

## Task 1: Terraform Infrastructure as Code

The Terraform configuration defines the staging GCP infrastructure with strict security controls:
1. **D0 Raw Landing (Google Cloud Storage Bucket)**:
   - Configured with `public_access_prevention` set to `"enforced"` and `uniform_bucket_level_access` set to `true`.
   - Utilizes strict bucket IAM conditions restricting administrative write permissions to a dedicated service account within a designated operational timeline.
2. **D1 Staged/Enforced (BigQuery Dataset & Table)**:
   - Defines a `student_onboarding_table` with a strict schema mirroring the onboarding data.
   - Implements **Row-Level Security (RLS)** via a `google_bigquery_row_access_policy` which restricts rows based on regional access (`local_support_authority_region = 'London'`) or administrative credentials.

### How to Run Terraform Validation Locally
To verify the configuration syntax without accessing a live Google Cloud Platform account:
1. Navigate to the `terraform/` directory:
   ```bash
   cd terraform
   ```
2. Initialize Terraform to download the required Google Cloud Platform provider plugins (version `>= 6.36.0`):
   ```bash
   terraform init
   ```
3. Format the Terraform files:
   ```bash
   terraform fmt
   ```
4. Validate the syntax of the configurations:
   ```bash
   terraform validate
   ```

---

## Task 2: Poka-Yoke "Fail-Closed" CI/CD Pipeline

The CI/CD pipeline defined in `pipeline/github-actions.yml` is a **Poka-Yoke** (mistake-proofing) gate. It is designed to halt immediately (**fail-closed**) if any issue is detected, preventing broken code or secrets from ever reaching staging or production environments.

It runs the following checks in sequence:
1. **Black Formatting Check**: Verifies Python code formatting.
2. **Flake8 Lint Gate**: Verifies syntax correctness and checks for PEP8 violations.
3. **Gitleaks Scan**: Scans the codebase for hardcoded API keys, tokens, or credentials.

### How to Run CI/CD Gates Locally
You can execute the pipeline checks locally using the following commands:
- **Format Verification**:
  ```bash
  black --check .
  ```
- **Lint Verification**:
  ```bash
  flake8 .
  ```
- **Security Secret Scanner**:
  ```bash
  gitleaks detect --no-git --verbose
  ```

---

## Task 3: Schema Mapping and DCYN Validation

The Django backend implements a strict validation API for onboarding students.

### Deconstructed Yes/No (DCYN) Validation Logic
The `StudentOnboardingSerializer` in [serializers.py](file:///c:/Users/S%20K/Desktop/GCP%20CLOUD%20PROJECT/HabotConnect_Project/django/student/serializers.py) implements the **Deconstructed Yes/No (DCYN)** validation architecture. Instead of failing immediately when the first invalid field is encountered, the serializer processes all required fields independently and resolves each to a strict boolean status (`True`/`False` or `Yes`/`No` validity). 

If any fields fail validation, the errors are collected into a single, structured dictionary and raised as a combined HTTP 400 response. This eliminates human ambiguity and allows client applications to receive complete validation feedback at once.

### Validation Parameters:
- `name`: Required, length must be between 2 and 100 characters.
- `age`: Required, must be an integer between 5 and 18 inclusive.
- `email`: Required, must be a valid email format.
- `phone`: Required, must be exactly 10 digits and only numeric characters.
- `consent`: Required, must be explicitly set to `True` (rejects `False` or missing values).

### How to Run Django Locally
1. Navigate to the `django/` directory:
   ```bash
   cd django
   ```
2. Run database migrations:
   ```bash
   python manage.py makemigrations student
   python manage.py migrate
   ```
3. Start the local development web server:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```
4. Test the API endpoints by posting payloads from `sample-data/student.json` using a tool like curl or Python's HTTP clients. The endpoint is:
   ```
   POST http://127.0.0.1:8000/api/student/
   ```
