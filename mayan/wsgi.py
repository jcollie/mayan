"""
WSGI config for mayan project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mayan.settings")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(PROJECT_DIR, '3rd_party_apps'))
sys.path.append(os.path.join(PROJECT_DIR, 'apps'))

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
  os.environ['DJANGO_ENVIRONMENT'] = environ['DJANGO_ENVIRONMENT']
  return _application(environ, start_response)
