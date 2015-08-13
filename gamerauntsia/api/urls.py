from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from gamerauntsia.api.handlers import MCHandler, MCTelebotHandler
	
auth = HttpBasicAuthentication(realm="Django Minecraft")
mc_handler = Resource(MCHandler)
mc_telebot_handler = Resource(MCTelebotHandler)
urlpatterns = patterns('',
    url(r'^get_minecraft_user/(?P<username>[-\w]+)/$', mc_handler),
    url(r'^send_mctelebot_msg/(?P<username>[-\w]+)/$', mc_telebot_handler),
)
