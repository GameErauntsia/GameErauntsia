from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^login/$', 'gamerauntsia.app.authentication.views.userLogin', name='login'),
    url(r'^register/$', 'gamerauntsia.app.authentication.views.register', name='register'),
    # url(r'^checkuser/$', 'gamerauntsia.app.authentication.views.checkuser', name='checkuser'),
)

if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': getattr(settings, 'MEDIA_ROOT', '')}),
    )