from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # change to your domain

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-env-secret')

# Database - example using PostgreSQL in prod
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
