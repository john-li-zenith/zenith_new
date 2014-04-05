"""
Django settings for zen project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DAJAXICE_MEDIA_PREFIX="dajaxice"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a+4z((xkno4pboaqaw1n-j2z6vt(h(3z9ls1j3t0$z-zf78k%a'

# SECURITY WARNING: don't run with debug turned on in production!
import socket
if '127.0.' not in socket.gethostbyname(socket.gethostname()):
   DEBUG = False
else:
   DEBUG = True


TEMPLATE_DEBUG = True

COMPRESS_ENABLED = True
COMPRESS_URL= '/static/'
COMPRESS_CSS_FILTERS=[
'compressor.filters.template.TemplateFilter',
'compressor.filters.css_default.CssAbsoluteFilter',
]

# default cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'Zenith'
    }
}

ALLOWED_HOSTS = []

TEMPLATE_DIRS=(os.path.join(BASE_DIR, 'templates'),)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ajax',
    'compressor',
    'dajaxice',
    'dajax',
)

# static files finders

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# template loader
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# static files finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'dajaxice.finders.DajaxiceFinder',
)

# template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

# session engine

SESSION_ENGINE = ('django.contrib.sessions.backends.signed_cookies')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zenith_new.urls'

WSGI_APPLICATION = 'zenith_new.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

if DEBUG:
  STATIC_URL = '/static/'

## heroku related settings
if not DEBUG:
  # Honor the 'X-Forwarded-Proto' header for request.is_secure()
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

  # Allow all host headers
  ALLOWED_HOSTS = ['*']

  # Static asset configuration
  STATIC_ROOT = 'staticfiles'
  STATIC_URL = '/static/'

  STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# SendGrid setting
if not DEBUG:
 EMAIL_HOST = 'smtp.sendgrid.net'
 EMAIL_HOST_USER = 'app21960119@heroku.com'
 EMAIL_HOST_PASSWORD = 'ujqqj5zd'
 EMAIL_PORT = 587
 EMAIL_USE_TLS = True
