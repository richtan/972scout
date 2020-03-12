from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SASS_PREPROCESSOR_ROOT = STATIC_ROOT
