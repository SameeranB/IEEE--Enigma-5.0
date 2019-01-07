"""
Django settings for Enigma project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$%c76--=hn7p@*n9luk+c%1qdek!^7z%-vl69p(uq6gb3b64hd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



#Setting up email config
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "ieee.enigma@gmail.com"
EMAIL_HOST_PASSWORD = "aruisgreat"
EMAIL_PORT = 587

# Google Recaptcha Credentials

GOOGLE_RECAPTCHA_SECRET_KEY = '6LeDz4UUAAAAAGpnJYAngvUwYJGfnnRyr61pcE0s'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LoginSignup',
    'Questions',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Enigma.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Enigma.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'enigma-5-test',
        'HOST': 'ds031912.mlab.com',
        'PORT': 31912,
        'USER': 'Sameeran',
        'PASSWORD': 'Sameeran1203',
        'AUTH_SOURCE': 'enigma-5-test',
        'AUTH_MECHANISM': 'SCRAM-SHA-1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',


]




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':8}
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


# STATIC
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]


# MEDIA
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

LOGIN_URL = 'LoginSignup/Login.html'
LOGIN_REDIRECT_URL = 'index.html'



# SESSION SETTINGS

SESSION_EXPIRE_SECONDS = 60
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True


# ALLAUTH SETTINGS
#
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_REQUIRED = True
#
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'index.html'
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'index.html'
#
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# ACCOUNT_PRESERVE_USERNAME_CASING = True
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT =5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT =300
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
#
# ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
# ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
#
# ACCOUNT_FORMS = {
#     'login': 'LoginSignup.forms.LoginForm',
#     'signup': 'LoginSignup.forms.UserForm',
#     'change_password': 'allauth.account.forms.ChangePasswordForm',
#     'reset_password': 'allauth.account.forms.ResetPasswordForm',
#
#
#
#
#}