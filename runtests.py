#!/usr/bin/env python
import django
from django.conf import settings
from django.core.management import call_command

TEST_SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'ALLOWED_HOSTS': [
        'testserver',
    ],
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'permissions',
        'permissions.tests',
    ],
    'PERMISSIONS': {
        'allow_staff': False,
    },
    'ROOT_URLCONF': 'permissions.tests.urls',
    'TEMPLATES': [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }],
    'TEST_RUNNER': 'django.test.runner.DiscoverRunner',
}

if django.VERSION < (1, 10):
    TEST_SETTINGS['MIDDLEWARE_CLASSES'] = []
else:
    TEST_SETTINGS['MIDDLEWARE'] = []

settings.configure(**TEST_SETTINGS)

if django.VERSION[:2] >= (1, 7):
    from django import setup
else:
    setup = lambda: None

setup()

call_command("test")
