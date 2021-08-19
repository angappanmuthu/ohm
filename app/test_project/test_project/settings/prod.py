from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k0zw6^*^r%+8&w%71@k((umdqu4%_uw%)@gp^@zo0pts@5mzof'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = "/static_files/"

STATIC_URL = "/static/"

ALLOWED_HOSTS = [
    '*'
    ]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR2,'debug.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}