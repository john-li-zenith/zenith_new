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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a+4z((xkno4pboaqaw1n-j2z6vt(h(3z9ls1j3t0$z-zf78k%a'

# SECURITY WARNING: don't run with debug turned on in production!
import socket
if 'heroku' not in socket.gethostname():
   DEBUG = True
else:
   DEBUG = False


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
    'compressor',
)

# static files finders

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
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
