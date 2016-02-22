# Django settings for gamerauntsia project.

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEFAULT_FROM_EMAIL = 'Game Erauntsia <no-reply@gamerauntsia.eus>'
BULETIN_FROM_EMAIL = DEFAULT_FROM_EMAIL
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[Game Erauntsia] '
DEFAULT_TO_EMAIL = 'Game Erauntsia <kontaktua@gamerauntsia.eus>'
EMAIL_SUBJECT = EMAIL_SUBJECT_PREFIX

EMAIL_HOST = 'smtp1.dc2.gpaas.net'


ADMINS = (
    ('Urtzi Odriozola', 'urtzi.odriozola@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'default_db',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/srv/data/web/vhosts/default/media/'
STATIC_ROOT = '/srv/data/web/vhosts/default/static/'

#TELEGRAM BOT
DIRNAME = '/home/csmant/django/gamerauntsia/'
TELEBOT_TOKEN = '107547414:AAEXaH2tSNcnaehNq_7NNbNKb1VfDbaa6Qs'
MC_CHAT_ID = '-31046360'
EDITOR_CHAT_ID = '-18452263'

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