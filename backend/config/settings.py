"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv 
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [] # TODO: Add frontend URLs here

# Email credentials
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = False

if (DEBUG):
    EMAIL_HOST = str(os.getenv('DEV_EMAIL_HOST'))
    EMAIL_HOST_USER = str(os.getenv('DEV_EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(os.getenv('DEV_EMAIL_HOST_PASSWORD'))
    EMAIL_PORT = str(os.getenv('DEV_EMAIL_PORT'))
else:
    EMAIL_HOST = str(os.getenv('PROD_EMAIL_HOST'))
    EMAIL_HOST_USER = str(os.getenv('PROD_EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = str(os.getenv('PROD_EMAIL_HOST_PASSWORD'))
    EMAIL_PORT = str(os.getenv('PROD_EMAIL_PORT'))
    EMAIL_USE_TLS = str(os.getenv('PROD_EMAIL_TLS'))

# Application definition

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.simple_history',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'simple_history',
    'djoser',
    'corsheaders',
    'drf_spectacular',
    'drf_spectacular_sidecar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_session_jwt.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF-Spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'University System Backend',
    'DESCRIPTION': 'A project by Keannu Bernasol',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # OTHER SETTINGS
}

DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_URL': 'reset_password/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_AUTHENTICATION_RULES': ['djoser.authentication.TokenAuthenticationRule'],
    'SERIALIZERS': {
        'user': 'accounts.serializers.CustomUserSerializer',
        'current_user': 'accounts.serializers.CustomUserSerializer',
        'user_create': 'accounts.serializers.UserRegistrationSerializer',
    },
}

# 1 Week Validity
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10080),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=10080)
}