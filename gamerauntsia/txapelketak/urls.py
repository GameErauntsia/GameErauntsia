from django.conf.urls import patterns, include, url
from gamerauntsia import settings

urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.txapelketak.views.index', name='txapelketak_index'),
    url(r'^(?P<slug>[-\w]+)$', 'gamerauntsia.txapelketak.views.txapelketa', name='txapelketa'),
)