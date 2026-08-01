# Project Name: HabotConnect Project
# Task Name: Student Onboarding Views Definition
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

from rest_framework import generics, status
from rest_framework.response import Response
from student.models import StudentOnboarding
from student.serializers import StudentOnboardingSerializer


class StudentOnboardingCreateView(generics.CreateAPIView):
    queryset = StudentOnboarding.objects.all()
    serializer_class = StudentOnboardingSerializer

    def create(self, http_request, *args, **kwargs):
        request_serializer = self.get_serializer(data=http_request.data)
        if request_serializer.is_valid(raise_exception=True):
            self.perform_create(request_serializer)
            headers = self.get_success_headers(request_serializer.data)
            return Response(
                request_serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
