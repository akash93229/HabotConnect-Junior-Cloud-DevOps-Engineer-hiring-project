# Project Name: HabotConnect Project
# Task Name: Django ASGI Server Configuration
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_asgi_application()
