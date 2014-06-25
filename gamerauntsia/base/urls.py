from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gamerauntsia.base.views', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)