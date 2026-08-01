# Project Name: HabotConnect Project
# Task Name: Django URL Routing Configuration
# Author: <YOUR FULL NAME>
# Contact: <YOUR EMAIL / PHONE>

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),
]
