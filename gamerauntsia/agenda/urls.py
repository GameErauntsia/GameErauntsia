from django.conf.urls import patterns, include, url


urlpatterns = patterns('gamerauntsia.agenda.views',
    url(r'^$', 'index', name='agenda_index'),
)
