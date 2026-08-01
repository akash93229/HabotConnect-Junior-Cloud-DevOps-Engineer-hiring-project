# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 3 - Django Student URL Routing

from django.urls import path
from student.views import StudentOnboardingCreateView

urlpatterns = [
    path(
        "api/student/",
        StudentOnboardingCreateView.as_view(),
        name="student-onboarding-create",
    ),
]
