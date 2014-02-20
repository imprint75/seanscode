import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('admin', 'admin@imprint75.com'),
)

MANAGERS = ADMINS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = '/home/sean/public_html/seanscode/public/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    '/home/sean/public_html/seanscode/public/seanscode/home/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'seanscode.urls'
TEMPLATE_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TEMPLATE_DIRS = (
    os.path.join(TEMPLATE_PATH, 'templates'),
)

INSTALLED_APPS = (
    'home',
    'work',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/nginx/error.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

# Echo Nest stuff
ECHO_NEST_BASE_URL = "http://developer.echonest.com/api/v4/"
EN_API_KEY = "OQWDHF6YVR619QHIA"
EN_CONSUMER_KEY = "81ad5073e9e9bf0dd989e8709580b376"
EN_SHARED_SECRET = "nEgXhmTsREOxjoETdkFqDw"
EN_USERNAME = 'sean'
DEFAULT_ARTIST = "Kassem Mosse"
