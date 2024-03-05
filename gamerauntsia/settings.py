# Django settings for gamerauntsia project.

import os
import raven

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

## General config
DEBUG = os.getenv("DEBUG", False)
TESTING = os.getenv("TESTING", False)
TEMPLATE_DEBUG = os.getenv("TEMPLATE_DEBUG", False)
TEMPLATE_DEBUG = DEBUG
SITE_ID = 1
LANGUAGE_CODE = "eu"
SECRET_KEY = os.getenv("SECRET_KEY")
POSTS_PER_PAGE = 10
GP_GROUP = "Gamerrak"  # Set your GamePlay editor group name
NEWS_GROUP = "Analistak"  # Set your blog editor group name
ENABLE_TRACKING = os.getenv("ENABLE_TRACKING") == "True"

## Email
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
BULETIN_FROM_EMAIL = DEFAULT_FROM_EMAIL
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = "[Game Erauntsia] "
DEFAULT_TO_EMAIL = os.getenv("DEFAULT_TO_EMAIL")
EMAIL_SUBJECT = EMAIL_SUBJECT_PREFIX

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# TELEGRAM BOT
TELEBOT_TOKEN = os.getenv("TG_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("TG_ADMIN_CHAT_ID")
MC_CHAT_ID = os.getenv("TG_MC_CHAT_ID")
EDITOR_CHAT_ID = os.getenv("TG_EDITOR_CHAT_ID")
PUBLIC_CHAT_ID = os.getenv("TG_PUBLIC_CHAT_ID")

# Twitter API
TWITTER_API_KEY = os.getenv("TW_API_KEY")
TWITTER_API_SECRET = os.getenv("TW_API_SECRET")
TWITTER_CONSUMER_KEY = TWITTER_API_KEY
TWITTER_CONSUMER_SECRET = TWITTER_API_SECRET
TWITTER_USERNAME = os.getenv("TW_USERNAME")
TWITTER_ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TW_ACCESS_TOKEN_SECRET")
TWITTER_MAXLENGTH = 140

# Facebook API
FB_APP_ID = os.getenv("FB_APP_ID")
FB_APP_SECRET = ""
FB_PAGE_ID = ""

# Mastodon API
MASTODON_CLIENT_ID = os.getenv("MA_CLIENT_ID")
MASTODON_CLIENT_SECRET = os.getenv("MA_CLIENT_SECRET")
MASTODON_USER_ACCESS_TOKEN = os.getenv("MA_USER_ACCESS_TOKEN")

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
NOCAPTCHA = True

# TWITCH
STREAMING_TWITCH_WEBHOOK_SECRET = os.getenv("STREAMING_TWITCH_WEBHOOK_SECRET")
STREAMING_TWITCH_CLIENT_ID = os.getenv("STREAMING_TWITCH_CLIENT_ID")
STREAMING_TWITCH_CLIENT_SECRET = os.getenv("STREAMING_TWITCH_CLIENT_SECRET")
## Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": os.getenv("MYSQL_PORT"),
    }
}

## Time
TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMINS = ()

MANAGERS = (("Urtzi Odriozola", "urtzi.odriozola@gmail.com"),)

## Paths
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_DOC_ROOT = STATIC_ROOT

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_DOC_ROOT = MEDIA_ROOT
ADMIN_MEDIA_PREFIX = os.path.join(BASE_DIR, "media/admin")

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    "django.contrib.flatpages",
    "mptt",
    "tagging",
    "photologue",
    "sortedm2m",
    "django_pagination_bootstrap",
    "tinymce",
    "emoticons",
    "registration",
    "django_forum_app",
    "django_comments",
    "facebookpagewriter",
    "bootstrapform",
    "star_ratings",
    "gamerauntsia",
    "gamerauntsia.jokoa",
    "gamerauntsia.gameplaya",
    "gamerauntsia.streaming",
    "gamerauntsia.base",
    "gamerauntsia.berriak",
    "gamerauntsia.kontaktua",
    "gamerauntsia.gamer",
    "gamerauntsia.templatetags",
    "gamerauntsia.aurkezpenak",
    "gamerauntsia.txapelketak",
    "gamerauntsia.getb",
    "gamerauntsia.zerbitzariak",
    "gamerauntsia.finished",
    "gamerauntsia.joko_itzulpenak",
    "gamerauntsia.jokoen_itzulpenak",
    "gamerauntsia.bazkidetza",
    "gamerauntsia.telegram",
    "gamerauntsia.pokedex",
    "gamerauntsia.podcast",
    "datetimewidget",
    "django_mobile",
    "django.contrib.admin",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    # 'rest_auth',
    # 'gamerauntsia.app.authentication',
    # 'gamerauntsia.app.services',
    "captcha",
    "corsheaders",
    "embed_video",
)

this = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
            "%s/templates"
            % this,
        ],
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "django_mobile.context_processors.flavour",
                "gamerauntsia.context_processors.fb_app_id",
                "gamerauntsia.context_processors.enable_tracking",
            ],
            "loaders": [
                # insert your TEMPLATE_LOADERS here
                "django_mobile.loader.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django_pagination_bootstrap.middleware.PaginationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django_mobile.middleware.MobileDetectionMiddleware",
    "django_mobile.middleware.SetFlavourMiddleware",
    "django.middleware.common.CommonMiddleware",
]

if DEBUG == "True" and not TESTING:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]

    def custom_show_toolbar(request):
        """Only show the debug toolbar to users with the superuser flag."""
        # return request.user.is_superuser
        if request.is_ajax():
            return False
        return True

    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INSTALLED_APPS += (
        "debug_toolbar",
        "template_debug",
    )

    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ]


CORS_ORIGIN_WHITELIST = (
    os.getenv("HOST_NAME"),
    "https://127.0.0.1",
)
CORS_ORIGIN_ALLOW_ALL = True

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'gamerauntsia.wsgi.application'

ROOT_URLCONF = "gamerauntsia.urls"

# EMAIL REGISTRATION
ACCOUNT_ACTIVATION_DAYS = 7

# Custom social user model
AUTH_USER_MODEL = "gamer.GamerUser"
PROFILE_PHOTO_DEFAULT_SLUG = "default-user"
# SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

# SOCIAL REGISTRATION
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

REGISTRATION_FORM = "gamerauntsia.gamer.forms.RecaptchaRegistrationForm"

# LOGIN URLS
LOGIN_URL = "/komunitatea/login/"
LOGIN_ERROR_URL = "/komunitatea/login-error/"

HOST = os.getenv("HOST_NAME") + "/"

USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "gamerauntsia.gamer.serializers.GameUserSerializer"
}

CORS_ORIGIN_ALLOW_ALL = True

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "store_to_file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/event.log"),
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "formatter": "simple",
            "filters": ["require_debug_false"],
        },
        "sentry": {
            "level": "ERROR",
            "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "": {
            "handlers": ["store_to_file", "sentry"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

# TINIYMCE
# TINYMCE_JS_ROOT = STATIC_ROOT + "js/tiny_mce/"
# TINYMCE_JS_URL = STATIC_URL + "js/tinymce/tinymce.min.js"
try:
    from .tiny_mce_settings import *
except:
    pass

## ADDITIONAL SETTINGS
try:
    from server_settings import *
except:
    pass

try:
    from .local_settings import *
except:
    pass
