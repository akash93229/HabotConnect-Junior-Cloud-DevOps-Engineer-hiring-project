# Project Name: HabotConnect Project
# Task Name: Student Onboarding Views Definition
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from student.models import StudentOnboarding
from student.serializers import StudentOnboardingSerializer


class StudentOnboardingCreateView(generics.CreateAPIView):
    """
    API View to handle student onboarding registration requests.
    Accepts POST requests, validates the input parameters using StudentOnboardingSerializer,
    and creates a new StudentOnboarding record.
    """

    queryset = StudentOnboarding.objects.all()
    serializer_class = StudentOnboardingSerializer

    def create(self, http_request, *args, **kwargs):
        """
        Processes incoming student onboarding POST payloads.
        Validates the inputs strictly using a Deconstructed Yes/No validation mechanism.
        Returns a HTTP 201 Created on success, or HTTP 400 Bad Request with a detailed
        dictionary of field validation failures on error.
        """
        request_serializer = self.get_serializer(data=http_request.data)

        # Perform validation; if it fails, it will raise serializers.ValidationError
        # which DRF automatically translates into HTTP 400 Bad Request response.
        if request_serializer.is_valid(raise_exception=True):
            self.perform_create(request_serializer)
            response_headers = self.get_success_headers(request_serializer.data)
            return Response(
                request_serializer.data,
                status=status.HTTP_201_CREATED,
                headers=response_headers,
            )
