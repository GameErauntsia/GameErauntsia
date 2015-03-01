from django.conf.urls import patterns, include, url
from gamerauntsia import settings
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from gamerauntsia.api.handlers import MCHandler
	
auth = HttpBasicAuthentication(realm="Django Minecraft")
mc_handler = Resource(MCHandler)	
urlpatterns = patterns('',
    url(r'^get_minecraft_user/(?P<username>[-\w]+)/$', mc_handler),
)