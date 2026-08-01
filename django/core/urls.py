# Project Name: HabotConnect Project
# Task Name: Django URL Routing Configuration
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("student.urls")),
]
