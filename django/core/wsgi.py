# Project Name: HabotConnect Project
# Task Name: Django WSGI Server Configuration
# Author: Akash Malviya
# Contact: akashmalviya244@gmail.com | 9753072646

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()
