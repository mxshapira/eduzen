"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os


def show_toolbar(request):
    return bool(os.getenv("DEBUG", False))


SITE_ID = 1
APPEND_SLASH = True
DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

ANYMAIL = os.environ.get("ANYMAIL")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "postgres"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASS", "postgres"),
        "HOST": os.environ.get("DB_SERVICE", "localhost"),
        "PORT": os.environ.get("DB_PORT", 5432),
    }
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.postgres",
]

THIRD_PARTY_APPS = [
    "captcha",
    "anymail",
    "crispy_forms",
    "ckeditor",
    "ckeditor_uploader",
    "solo",
    "robots",
    "djmoney",
    "rest_framework",
    "django_extensions",
]

# Application definition
APPS = [
    "config",
    "blog",
    "api",
    "expenses",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ]
        },
    }
]

WSGI_APPLICATION = "website.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = "/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]

CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min."
CKEDITOR_UPLOAD_PATH = "/"
CKEDITOR_CONFIGS = {
    "awesome_ckeditor": {"toolbar": "full"},
    "default": {
        "toolbar": "full",
        "autoParagraph": "false",
        "breakBeforeOpen": "false",
        "breakAfterOpen": "false",
        "breakBeforeClose": "false",
        "breakAfterClose": "false",
        "enterMode": "false",
        "extraPlugins": ",".join(["codesnippet"]),
    },
    "autoParagraph": "false",
}

# Crispy Forms
CRISPY_TEMPLATE_PACK = "bootstrap3"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 10
CAPTCHA_TIMEOUT = 1
CAPTCHA_LETTER_ROTATION = (-45, 45)
