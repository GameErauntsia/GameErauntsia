from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('gamerauntsia.bazkidetza.views',
	url(r'^$', 'index', name='bazkidetza'),
	url(r'^izan-bazkide/$', 'create_bazkidea', name='create_bazkidea'),
	url(r'^eskaera-egin/(?P<eskaintza_id>[\d]+)/$', 'create_eskaera', name='create_eskaera'),
    url(r'^ordainketa-eginda/$', 'payment_done', name='payment_done'),
	url(r'^eskaintza/(?P<slug>[-\w]+)/$', 'eskaintza', name='eskaintza'),
)