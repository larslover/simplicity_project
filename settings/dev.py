from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Optionally, you can override DB for dev if needed
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Local static/media settings if needed
STATICFILES_DIRS = [BASE_DIR / 'static']
