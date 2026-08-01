# Project Name: HabotConnect Project
# Task Name: Student Onboarding Model Definition
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

from django.db import models


class StudentOnboarding(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_email_address = models.EmailField()
    # stored as string to preserve leading zeros if any
    student_phone_number = models.CharField(max_length=10)
    guardian_consent_given = models.BooleanField(default=False)
    educational_institution_name = models.CharField(max_length=150)
    parent_guardian_full_name = models.CharField(max_length=100)
    learning_difficulty_description = models.TextField(blank=True, null=True)
    local_support_authority_region = models.CharField(max_length=100)
    record_created_at_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} (Age: {self.student_age})"
