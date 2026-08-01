# Project Name: HabotConnect Project
# Task Name: Student App URL Routing Configuration
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

from django.urls import path
from student.views import StudentOnboardingCreateView

urlpatterns = [
    path(
        "api/student/",
        StudentOnboardingCreateView.as_view(),
        name="student-onboarding-create",
    ),
]
