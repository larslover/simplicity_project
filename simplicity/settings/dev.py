from .base import *

DEBUG = True

# Temporary key for local development
SECRET_KEY = 'dev-secret-key'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Local database (already in base, optional override)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
