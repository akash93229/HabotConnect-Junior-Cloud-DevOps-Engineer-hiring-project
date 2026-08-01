# Project Name: HabotConnect Project
# Task Name: Student App URL Routing Configuration
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

from django.urls import path
from student.views import StudentOnboardingCreateView

urlpatterns = [
    path(
        "api/student/",
        StudentOnboardingCreateView.as_view(),
        name="student-onboarding-create",
    ),
]
