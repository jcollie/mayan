# -*- coding: utf-8 -*-
from .base import *  # pyflakes.ignore

DEBUG = True
TEMPLATE_DEBUG = True

# Email ------------------------------------------------------------------------

# TODO: Reemplazar por un servidor smtp integrado en Django
# Configuración para mailcatcher
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST, EMAIL_PORT = '127.0.0.1', 1025  # Work with mailcatcher

DEFAULT_FROM_EMAIL = 'info@web.com'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': location('var/cache')
    }
}

INTERNAL_IPS = ('127.0.0.1',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
try:
    import rosetta
    INSTALLED_APPS += ('rosetta',)
except ImportError:
    pass

try:
    import django_extensions
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass

try:
    import debug_toolbar
    #INSTALLED_APPS +=('debug_toolbar',)
except ImportError:
    pass        

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

WSGI_AUTO_RELOAD = True
if 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

