from .base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # matches github actions config
        'NAME': 'djftest',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'TEST': {
            'NAME': 'djftest',
        },
    },
}
