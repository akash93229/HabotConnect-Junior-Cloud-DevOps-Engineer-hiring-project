# Full Name: Akash Malviya
# Contact: akashmalviya244@gmail.com
# Phone: 9753072646
# Project: HabotConnect Junior Cloud and DevOps Engineer
# Submission Date: 01/08/2026
# Task: Task 3 - Django ASGI Server Configuration

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_asgi_application()
