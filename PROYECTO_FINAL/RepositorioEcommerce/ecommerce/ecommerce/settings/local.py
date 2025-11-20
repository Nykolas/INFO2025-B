from .base import *

SECRET_KEY = 'django-insecure-yuhihp2taa46(i_di^znj=m7cd(dek(y#rr0n+=9n!w^ver%o9'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

