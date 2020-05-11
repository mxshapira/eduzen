"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from .base import *  # NOQA

DEBUG = True
SECRET_KEY = "unsecret_key"

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # NOQA
INSTALLED_APPS += ["debug_toolbar"]  # NOQA
INTERNAL_IPS = ("*",)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "mydatabase"}}
