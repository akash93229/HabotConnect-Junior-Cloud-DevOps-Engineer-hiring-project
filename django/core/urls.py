# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 3 - Django Root URL Configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("student.urls")),
]
