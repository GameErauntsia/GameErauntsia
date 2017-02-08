from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^get_minecraft_user$', mc_whitelist),
    url(r'^send_mctelebot_msg/(?P<username>[-\w]+)/$', mc_telebot),
)
