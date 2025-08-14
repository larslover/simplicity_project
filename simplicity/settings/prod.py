import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'simplicity.pythonanywhere.com',
    'www.simplicitysapps.com',
]

# Secret key from environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-env-secret')

# Static files
STATIC_ROOT = BASE_DIR / 'simplicity' / 'staticfiles'


# Email using business account
# Email using business account
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'larsroaldlover@gmail.com'
EMAIL_HOST_PASSWORD = 'whrbrshoxxjctqgh'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER




# MySQL database on PythonAnywhere (adjust username and DB)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'yourusername$simplicity'),
        'USER': os.getenv('DB_USER', 'yourusername'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'yourusername.mysql.pythonanywhere-services.com'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
