"""
Django settings for testapp project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=p!iz2&djy0c$e%i$p&e_=$&_fs-mjz6p)s1)4vp%r@5ih=&h$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['yagi.tsolpd.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'applicationinsights.django.ApplicationInsightsMiddleware',
]

ROOT_URLCONF = 'testapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'testapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

APPLICATION_INSIGHTS = {
    # (required) Your Application Insights instrumentation key
    'ikey': "0b6874ae-6834-4e5b-a4de-b314b1297153",

    # (optional) By default, request names are logged as the request method
    # and relative path of the URL.  To log the fully-qualified view names
    # instead, set this to True.  Defaults to False.
    'use_view_name': True,

    # (optional) To log arguments passed into the views as custom properties,
    # set this to True.  Defaults to False.
    'record_view_arguments': True,

    # (optional) Exceptions are logged by default, to disable, set this to False.
    'log_exceptions': False,

    # (optional) Events are submitted to Application Insights asynchronously.
    # send_interval specifies how often the queue is checked for items to submit.
    # send_time specifies how long the sender waits for new input before recycling
    # the background thread.
    'send_interval': 1.0, # Check every second
    'send_time': 3.0, # Wait up to 3 seconds for an event

    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # The application insights handler is here
        'appinsights': {
            'class': 'applicationinsights.django.LoggingHandler',
            'level': 'ERROR'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['appinsights'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}

