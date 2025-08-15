import os
from pathlib import Path
from .base import *

DEBUG = False

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # adjust to root project folder

ALLOWED_HOSTS = [
    'simplicity.pythonanywhere.com',
    'www.simplicitysapps.com',
]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-secret-key')

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER', 'default@example.com')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'default@example.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'default_db_name'),
        'USER': os.environ.get('DB_USER', 'default_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = '/home/LarsLover/static'  # folder on PythonAnywhere where static files will be collected

# Security
SECURE_SSL_REDIRECT = True
