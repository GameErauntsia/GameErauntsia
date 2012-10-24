from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blenderEUS.base.views', name='index'),
    # url(r'^blenderEUS/', include('blenderEUS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)