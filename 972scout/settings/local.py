from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    'sass_processor',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

SASS_PREPROCESSOR_ROOT = STATIC_ROOT
