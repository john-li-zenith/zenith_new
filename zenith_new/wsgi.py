"""
WSGI config for zen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
from zenith_new.settings import DEBUG
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zenith_new.settings")

if DEBUG:
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()

if not DEBUG:
   from dj_static import Cling
   from django.core.wsgi import get_wsgi_application
   application = Cling(get_wsgi_application())
