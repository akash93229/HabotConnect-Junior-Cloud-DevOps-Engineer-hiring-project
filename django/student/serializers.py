# Project Name: HabotConnect Project
# Task Name: Student Onboarding Serializer and Validation
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

from rest_framework import serializers
from student.models import StudentOnboarding
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class StudentOnboardingSerializer(serializers.ModelSerializer):
    """
    DRF ModelSerializer for StudentOnboarding that enforces strict field validation limits.
    Implements a custom 'DCYN' (Deconstructed Yes/No) validation logic to collect and report
    all validation errors concurrently.
    """

    # Explicit mapping of API fields to model fields with strict validation constraints
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

    def validate_phone(self, phone_number_value):
        """
        Validate that the phone number is exactly 10 digits and consists of digits only.
        """
        if len(phone_number_value) != 10 or not phone_number_value.isdigit():
            raise serializers.ValidationError(
                "The phone number must be exactly 10 digits and contain only numeric characters."
            )
        return phone_number_value

    def validate(self, validation_attributes):
        """
        Implements the Deconstructed Yes/No (DCYN) validation logic.
        Evaluates each attribute individually to yield a strict boolean result (Yes/No).
        Accumulates all validation errors to present a full list of issues to the client.
        """
        validation_error_dictionary = {}

        # 1. Deconstructed validation for Name
        student_name_value = validation_attributes.get("student_name", "")
        if not student_name_value:
            validation_error_dictionary["name"] = (
                "The name field is required and cannot be empty."
            )
        elif len(student_name_value) < 2 or len(student_name_value) > 100:
            validation_error_dictionary["name"] = (
                f"The name must be between 2 and 100 characters. "
                f"Current length: {len(student_name_value)}."
            )

        # 2. Deconstructed validation for Age
        student_age_value = validation_attributes.get("student_age")
        if student_age_value is None:
            validation_error_dictionary["age"] = "The age field is required."
        elif student_age_value < 5 or student_age_value > 18:
            validation_error_dictionary["age"] = (
                f"The age must be between 5 and 18 years inclusive. "
                f"Provided age: {student_age_value}."
            )

        # 3. Deconstructed validation for Email
        student_email_value = validation_attributes.get("student_email_address", "")
        if not student_email_value:
            validation_error_dictionary["email"] = "The email field is required."
        else:
            try:
                validate_email(student_email_value)
            except ValidationError:
                validation_error_dictionary["email"] = (
                    f"The provided email '{student_email_value}' is not a valid email address."
                )

        # 4. Deconstructed validation for Phone
        student_phone_value = validation_attributes.get("student_phone_number", "")
        if not student_phone_value:
            validation_error_dictionary["phone"] = "The phone field is required."
        elif len(student_phone_value) != 10 or not student_phone_value.isdigit():
            validation_error_dictionary["phone"] = (
                f"The phone number must be exactly 10 digits and contain only numeric characters. "
                f"Provided: '{student_phone_value}'."
            )

        # 5. Deconstructed validation for Consent
        guardian_consent_value = validation_attributes.get("guardian_consent_given")
        if guardian_consent_value is None or guardian_consent_value is False:
            validation_error_dictionary["consent"] = (
                "Onboarding cannot proceed without parental/guardian consent. "
                "The consent field must be explicitly set to True."
            )

        # 6. Deconstructed validation for School Name
        school_name_value = validation_attributes.get(
            "educational_institution_name", ""
        )
        if not school_name_value:
            validation_error_dictionary["school_name"] = (
                "The school_name field is required."
            )

        # 7. Deconstructed validation for Parent/Guardian Name
        parent_guardian_name_value = validation_attributes.get(
            "parent_guardian_full_name", ""
        )
        if not parent_guardian_name_value:
            validation_error_dictionary["parent_guardian_name"] = (
                "The parent_guardian_name field is required."
            )

        # 8. Deconstructed validation for LSA Region
        lsa_region_value = validation_attributes.get(
            "local_support_authority_region", ""
        )
        if not lsa_region_value:
            validation_error_dictionary["lsa_region"] = (
                "The lsa_region field is required."
            )

        # Raise all validation errors simultaneously if any check resolved to False
        if validation_error_dictionary:
            raise serializers.ValidationError(validation_error_dictionary)

        return validation_attributes
