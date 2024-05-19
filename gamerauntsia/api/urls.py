from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r"^get_minecraft_user$", mc_whitelist),
    re_path(r"^send_mctelebot_msg/(?P<username>[-\w]+)/$", mc_telebot),
]
