from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.aurkezpenak.views.index', name='aurkezpenak_index'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.aurkezpenak.views.aurkezpena', name='aurkezpena'),
)
