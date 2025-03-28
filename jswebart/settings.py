"""
Django settings for jswebart project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['.vercel.app','.now.sh', 'jswebart.com','www.jswebart.com', '127.0.0.1', 'localhost']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'core',
    'portfolio',
    'blog',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_recaptcha',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jswebart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'jswebart.context_processors.subscription_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'jswebart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# Add these at the top of your settings.py

# Replace the DATABASES section of your settings.py with this
# tmpPostgres = urlparse("DATABASE_URL")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST')
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


import os
if DEBUG:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        'jswebart/static'
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:    
    STATIC_URL = 'https://jitbherwaniofficial.github.io/jswebart-staticfiles/'

# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME', default=None),
    'API_KEY': config('API_KEY', default=None),
    'API_SECRET': config('API_SECRET_KEY', default=None),
    'RESOURCE_TYPE': 'auto',  # or 'auto' for mixed file types
}

CLOUD_NAME = config('CLOUD_NAME')

# Cloudinary for static and media files
# STORAGES = {
#     "default": {
#         "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "cloudinary_storage.storage.StaticHashedCloudinaryStorage",
#     },
# }

# STATIC_URL = f'https://res.cloudinary.com/{config("CLOUD_NAME")}/static/'
# STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = f'https://res.cloudinary.com/{CLOUD_NAME}/media/'


# Static and Media URLs (Cloudinary will handle the URL generation)
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1

# Email Configuration
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# DEFAULT_FROM_EMAIL = 'Jit Design <darkenergy120892@gmail.com>'

# Django>=3.0,<5.0

RECAPTCHA_PUBLIC_KEY = 'your_site_key_here'    # From Google reCAPTCHA
RECAPTCHA_PRIVATE_KEY = 'your_secret_key_here' # From Google reCAPTCHA

