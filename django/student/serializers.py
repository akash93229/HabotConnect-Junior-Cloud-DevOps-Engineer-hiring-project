# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 3 - Django Student Onboarding Serializer with DCYN Validation

from rest_framework import serializers
from student.models import StudentOnboarding
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class StudentOnboardingSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source="student_name",
        min_length=2,
        max_length=100,
        required=True,
        error_messages={
            "required": "The name field is required.",
            "min_length": "The name must be at least 2 characters long.",
            "max_length": "The name cannot exceed 100 characters.",
        },
    )
    age = serializers.IntegerField(
        source="student_age",
        required=True,
        error_messages={"required": "The age field is required."},
    )
    email = serializers.EmailField(
        source="student_email_address",
        required=True,
        error_messages={
            "required": "The email field is required.",
            "invalid": "Provide a valid email address format.",
        },
    )
    phone = serializers.CharField(
        source="student_phone_number",
        required=True,
        error_messages={"required": "The phone field is required."},
    )
    consent = serializers.BooleanField(
        source="guardian_consent_given",
        required=True,
        error_messages={"required": "The consent field is required."},
    )
    school_name = serializers.CharField(
        source="educational_institution_name",
        max_length=150,
        required=True,
        error_messages={"required": "The school_name field is required."},
    )
    parent_guardian_name = serializers.CharField(
        source="parent_guardian_full_name",
        max_length=100,
        required=True,
        error_messages={"required": "The parent_guardian_name field is required."},
    )
    learning_difficulty_description = serializers.CharField(
        required=False, allow_null=True, allow_blank=True
    )
    lsa_region = serializers.CharField(
        source="local_support_authority_region",
        max_length=100,
        required=True,
        error_messages={"required": "The lsa_region field is required."},
    )

    class Meta:
        model = StudentOnboarding
        fields = [
            "name",
            "age",
            "email",
            "phone",
            "consent",
            "school_name",
            "parent_guardian_name",
            "learning_difficulty_description",
            "lsa_region",
        ]

    def validate_phone(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def validate(self, attrs):
        # DCYN: collect all errors before raising, so client gets everything at once
        errors = {}

        name = attrs.get("student_name", "")
        if not name:
            errors["name"] = "The name field is required and cannot be empty."
        elif len(name) < 2 or len(name) > 100:
            errors["name"] = (
                f"Name must be between 2 and 100 characters (got {len(name)})."
            )

        age = attrs.get("student_age")
        if age is None:
            errors["age"] = "The age field is required."
        elif age < 5 or age > 18:
            errors["age"] = f"Age must be between 5 and 18 (got {age})."

        email = attrs.get("student_email_address", "")
        if not email:
            errors["email"] = "The email field is required."
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = f"'{email}' is not a valid email address."

        phone = attrs.get("student_phone_number", "")
        if not phone:
            errors["phone"] = "The phone field is required."
        elif len(phone) != 10 or not phone.isdigit():
            errors["phone"] = f"Phone must be exactly 10 digits (got '{phone}')."

        # consent must be explicitly True -- False or missing both block onboarding
        consent = attrs.get("guardian_consent_given")
        if not consent:
            errors["consent"] = "Guardian consent must be explicitly set to True."

        if not attrs.get("educational_institution_name", ""):
            errors["school_name"] = "The school_name field is required."

        if not attrs.get("parent_guardian_full_name", ""):
            errors["parent_guardian_name"] = (
                "The parent_guardian_name field is required."
            )

        if not attrs.get("local_support_authority_region", ""):
            errors["lsa_region"] = "The lsa_region field is required."

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
