# Project Name: HabotConnect Project
# Task Name: Student Onboarding Model Definition
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

from django.db import models


class StudentOnboarding(models.Model):
    """
    Django Model representing the onboarding registration of a student.
    Contains demographic, contact, guardian consent, and regional educational details.
    """

    # Core demographic and contact fields
    student_name = models.CharField(
        max_length=100, help_text="The full legal name of the student being onboarded."
    )
    student_age = models.IntegerField(
        help_text="The age of the student (must be between 5 and 18 inclusive)."
    )
    student_email_address = models.EmailField(
        help_text="The contact email address for student-related notifications."
    )
    student_phone_number = models.CharField(
        max_length=10,
        help_text="The 10-digit numeric mobile or home telephone contact number.",
    )

    # Onboarding authorization field
    guardian_consent_given = models.BooleanField(
        default=False,
        help_text="Flag indicating if the parent or legal guardian has formally given consent.",
    )

    # Educational and regional context fields
    educational_institution_name = models.CharField(
        max_length=150,
        help_text="The name of the educational institution/school the student is enrolled in.",
    )
    parent_guardian_full_name = models.CharField(
        max_length=100,
        help_text="The full legal name of the primary parent or legal guardian.",
    )
    learning_difficulty_description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of any learning difficulties or special accommodations needed.",
    )
    local_support_authority_region = models.CharField(
        max_length=100,
        help_text="The Local Support Authority (LSA) region overseeing educational support.",
    )

    # Metadata fields
    record_created_at_timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when this onboarding record was created.",
    )

    def __str__(self):
        return f"{self.student_name} (Age: {self.student_age}) - Onboarding Record"
