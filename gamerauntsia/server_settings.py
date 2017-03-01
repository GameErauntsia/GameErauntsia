# Django settings for gamerauntsia project.

import os
import raven

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = 'Game Erauntsia <no-reply@gamerauntsia.eus>'
BULETIN_FROM_EMAIL = DEFAULT_FROM_EMAIL
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[Game Erauntsia] '
DEFAULT_TO_EMAIL = 'Game Erauntsia <kontaktua@gamerauntsia.eus>'
EMAIL_SUBJECT = EMAIL_SUBJECT_PREFIX

EMAIL_HOST = 'localhost'


ADMINS = (
    ('Urtzi Odriozola', 'urtzi.odriozola@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gamerauntsia',                      # Or path to database file if using sqlite3.
        'USER': 'ge_user',                      # Not used with sqlite3.
        'PASSWORD': 'Gamerrakgara2014',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = "/home/ge/django/media/"
STATIC_ROOT = "/home/ge/django/static/"


RAVEN_CONFIG = {
    'dsn': 'https://63aa9724019d48478e7dc2e6230806bc:9ea7e51ed77a41fdba698f739f0e8b7c@sentry.codesyntax.com/32',
}

SECRET_KEY = 'c%@)ihbb+u5i3%4v4f_@78g7s9k$#lo^yixhpjnh=f1%l2-5sv'


#TELEGRAM BOT
DIRNAME = '/home/ge/buildout/src/gamerauntsia/'
TELEBOT_TOKEN = '107547414:AAEXaH2tSNcnaehNq_7NNbNKb1VfDbaa6Qs'
ADMIN_CHAT_ID = '-1001067796173'
MC_CHAT_ID = '-1001043512672'
EDITOR_CHAT_ID = '-1001058016648'
PUBLIC_CHAT_ID = '-1001060976302'

#Twitter API
TWITTER_API_KEY = 'QMPvaez5H2KpBWP9CwnfYTU2M'
TWITTER_API_SECRET = 'PIqjFcoSLiaB8RE20KcUjrqI4RAYb8RwzGIfHy43D8zhJttqcc'
TWITTER_CONSUMER_KEY = TWITTER_API_KEY
TWITTER_CONSUMER_SECRET = TWITTER_API_SECRET
TWITTER_USERNAME = 'gamerauntsia'
TWITTER_ACCESS_TOKEN = '2663678179-XsYD1snwUqvc7VJryppOPJFbAwO3iFGLsNsaMkE'
TWITTER_ACCESS_TOKEN_SECRET = 'ZmwQ82fbfIGWY8voHbzfIYKmkT8egMcSOIWGlGE8cZeyD'
TWITTER_MAXLENGTH = 140

#Facebook API
FB_APP_ID = '1466131240329239'
FACEBOOK_APP_ID = FB_APP_ID
FB_APP_SECRET = '69cf0d955b37aa12cb0f30857e250fc4'
FB_PAGE_ID = '326435330850157'

RECAPTCHA_PUBLIC_KEY = '6LeG_hgTAAAAAMcQ4Lkp0Gv_vP-xoTjbN4QpGmo1'
RECAPTCHA_PRIVATE_KEY = '6LeG_hgTAAAAALBOvGMyyohi5g7Z9z7j1n4bsE5s'
NOCAPTCHA = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'store_to_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/ge/django/logs/event.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'simple',
            'filters': ['require_debug_false'],
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['store_to_file', 'sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
