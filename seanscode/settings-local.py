import os
from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'admin@imprint75.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seanscode',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = '/Users/seansmith/Documents/DEV/site/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '/Users/seansmith/Documents/DEV/site/seanscode/home/static/',
)

SECRET_KEY = '3f&x%c#+b9uzek4r^g=0ggx1l53pm8-^c3k##b^e4y085%3yip'

TEMPLATE_DIRS = (
    "/Users/seansmith/Dev/projects/seanscode2/seanscode/templates"
)

# Echo Nest stuff
ECHO_NEST_BASE_URL = "http://developer.echonest.com/api/v4/"
EN_API_KEY = "OQWDHF6YVR619QHIA"
EN_CONSUMER_KEY = "81ad5073e9e9bf0dd989e8709580b376"
EN_SHARED_SECRET = "nEgXhmTsREOxjoETdkFqDw"
EN_USERNAME = 'sean'
DEFAULT_ARTIST = "Kassem Mosse"
