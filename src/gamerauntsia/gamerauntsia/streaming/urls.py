from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r"^twitch-callback$", twitch_subscription_callback),
    re_path(r"^(?P<slug>[-\w]+)$", streaming, name="streaming"),
]
