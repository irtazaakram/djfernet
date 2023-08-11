import platform

from .base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # matches travis config
        'NAME': 'djftest',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'TEST': {
            'NAME': 'djftest',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
        },
    },
}
