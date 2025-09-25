from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgrasql',
        'NAME': BASE_DIR / 'db.postgresql',
    }
}