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

EMAIL_HOST = os.environ.get('EMAIL_HOST')


ADMINS = (
    ('Urtzi Odriozola', 'urtzi.odriozola@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ.get('DB_NAME'),                      # Or path to database file if using sqlite3.
        'USER': os.environ.get('DB_USER'),                      # Not used with sqlite3.
        'PASSWORD': os.environ.get('DB_PASSWORD'),                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'eu'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/srv/data/web/vhosts/default/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/srv/data/web/vhosts/default/static/'

STATIC_DOC_ROOT = STATIC_ROOT
MEDIA_DOC_ROOT = MEDIA_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX='/media/admin/'

POSTS_PER_PAGE = 10

GP_GROUP = 'Gamerrak' #Set your GamePlay editor group name
NEWS_GROUP = 'Analistak' #Set your blog editor group name

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'mptt',
    'tagging',
    'photologue',
    'pagination',
    'tinymce',
    'emoticons',
    'cssocialuser',
    'registration',
    'social_auth',
    'django_simple_forum',
    'django_comments',
    'facebookpagewriter',
    'gamerauntsia',
    'gamerauntsia.gameplaya',
    'gamerauntsia.base',
    'gamerauntsia.berriak',
    'gamerauntsia.kontaktua',
    'gamerauntsia.jokoa',
    'gamerauntsia.gamer',
    'gamerauntsia.auto_gameplay',
    'gamerauntsia.templatetags',
    'gamerauntsia.aurkezpenak',
    'gamerauntsia.txapelketak',
    'gamerauntsia.getb',
    'gamerauntsia.zerbitzariak',
    'gamerauntsia.log',
    'grappelli',
    'datetimewidget',
    'django_bootstrap_calendar',
    'django_messages',
    'django.contrib.admin',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'gamerauntsia.context_processors.fb_app_id',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5^!cvi0%23pm%3jo6cu1kmhv=am$3+@_+g@q%sx=mej#2_h41z'

# List of callables that know how to import templates from various sources.
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
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.locale.LocaleMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'gamerauntsia.wsgi.application'

this = os.path.dirname(os.path.abspath(__file__))
my_media_url=os.path.join(os.path.dirname(__file__), "media")

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '%s/templates' % this,
)

ROOT_URLCONF = 'gamerauntsia.urls'

#EMAIL REGISTRATION
ACCOUNT_ACTIVATION_DAYS = 7

# Custom social user model
AUTH_USER_MODEL = 'gamer.GamerUser'
PROFILE_PHOTO_DEFAULT_SLUG = 'default-user'

#SOCIAL REGISTRATION
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.social.load_extra_data',
    'cssocialuser.models.get_user_data',
)

#TINYMCE PATH
TINYMCE_JS_ROOT = STATIC_ROOT + "js/tinymce/"
TINYMCE_JS_URL = STATIC_URL + "js/tinymce/tinymce.min.js"

#TELEGRAM BOT
DIRNAME = '/home/csmant/django/gamerauntsia/'
TELEBOT_TOKEN = os.environ.get('TELEBOT_TOKEN')
MC_CHAT_ID = os.environ.get('MC_CHAT_ID')
EDITOR_CHAT_ID = os.environ.get('EDITOR_CHAT_ID') 

#Twitter API
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET')
TWITTER_CONSUMER_KEY = TWITTER_API_KEY
TWITTER_CONSUMER_SECRET = TWITTER_API_SECRET
TWITTER_USERNAME = 'gamerauntsia'
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
TWITTER_MAXLENGTH = 140

#Facebook API
FB_APP_ID = os.environ.get('FB_APP_ID')
FACEBOOK_APP_ID = FB_APP_ID
FB_APP_SECRET = os.environ.get('FB_APP_SECRET')
FB_PAGE_ID = os.environ.get('FB_PAGE_ID')

FACEBOOK_EXTENDED_PERMISSIONS = [
    'publish_stream',
]

#LOGIN URLS
LOGIN_URL          = '/erabiltzaileak/login/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

HOST = 'http://gamerauntsia.eus/'

USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'www.gamerauntsia.eus','gamerauntsia.eus']

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
   from tiny_mce_settings import *
except:
   pass

try:
    from local_settings import *
except:
    pass
