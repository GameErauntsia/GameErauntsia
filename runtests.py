#!/usr/bin/env python

import sys
import os
import django
from django.conf import settings
from django.test.utils import get_runner


APP_NAME = 'gamerauntsia'

settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'gamerauntsia',
                'USER': 'travis',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            }
        },
        USE_TZ=True,
        ROOT_URLCONF='{0}.urls'.format(APP_NAME),
        STATIC_URL='/static/',
        MEDIA_URL='/media/',
        FB_APP_SECRET='345sefsdfasdf2342234',
        FB_APP_ID='123456789',
        TELEBOT_TOKEN='110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw',
        HOST='gamerauntsia.eus',
        ADMIN_CHAT_ID='122346632',
        SITE_ID=1,
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.sitemaps',
            'django.contrib.humanize',
            'django.contrib.flatpages',
            'mptt',
            'tagging',
            'photologue',
            'sortedm2m',
            'pagination_bootstrap',
            'tinymce',
            'emoticons',
            'registration',
            'django_forum_app',
            'django_comments',
            'facebookpagewriter',
            'bootstrapform',
            'star_ratings',
            'gamerauntsia',
            'gamerauntsia.jokoa',
            'gamerauntsia.gameplaya',
            'gamerauntsia.base',
            'gamerauntsia.berriak',
            'gamerauntsia.kontaktua',
            'gamerauntsia.gamer',
            'gamerauntsia.templatetags',
            'gamerauntsia.aurkezpenak',
            'gamerauntsia.txapelketak',
            'gamerauntsia.getb',
            'gamerauntsia.zerbitzariak',
            'gamerauntsia.finished',
            'gamerauntsia.jokoen_itzulpenak',
            'gamerauntsia.bazkidetza',
            'gamerauntsia.log',
            'datetimewidget',
            'django_bootstrap_calendar',
            'django_messages',
            'django_mobile',
            'django.contrib.admin',
            'rest_framework',
            'rest_framework.authtoken',
            # 'rest_auth',
            'gamerauntsia.app.authentication',
            'gamerauntsia.app.services',
            'captcha',
            'corsheaders',
            'podcasting',
        ),
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    # insert your TEMPLATE_DIRS here
                    os.path.join(os.path.dirname(__file__), "templates"),
                ],
                'OPTIONS': {
                    'context_processors': [
                        # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                        # list if you haven't customized them:
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.request",
                    ],
                    'loaders': [
                        # insert your TEMPLATE_LOADERS here
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]
                },
            },
        ],
        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'pagination_bootstrap.middleware.PaginationMiddleware',
        ],
        TEMPLATE_LOADERS = (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
        )
)


if hasattr(django, 'setup'):
    django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests([APP_NAME])
if failures:
    sys.exit(failures)
