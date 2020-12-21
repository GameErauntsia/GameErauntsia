from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^twitch-callback$', twitch_subscription_callback)
]
