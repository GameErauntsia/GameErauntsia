from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^get_minecraft_user$", mc_whitelist),
    url(r"^send_mctelebot_msg/(?P<username>[-\w]+)/$", mc_telebot),
]
