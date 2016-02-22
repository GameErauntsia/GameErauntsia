from django.conf.urls import patterns, include, url

urlpatterns = patterns('gamerauntsia.getb.views',
	url(r'^$', 'index', name='getb_index'),
    url(r'^(?P<slug>[-\w]+)$', 'atala', name='getb_atala'),
)
