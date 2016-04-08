from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^youtuberrak/', 'gamerauntsia.gamer.views.youtuberrak', name='gamer_youtuberrak'),
                       url(r'^$', 'gamerauntsia.gamer.views.index', name='gamer_index'),

                       url(r'^gamer_add_favorite_game/(?P<slug>[-\w]+)$', 'gamerauntsia.gamer.views.add_favorite_game',
                           name='gamer_add_favorite_game'),
                       url(r'^(?P<username>[-\w]+)$', 'gamerauntsia.gamer.views.profile', name='gamer_profile'),

                       )
