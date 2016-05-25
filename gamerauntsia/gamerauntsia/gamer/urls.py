from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('gamerauntsia.gamer.views',
	url(r'^$', 'community', name='komunitatea'),
    url(r'^youtuberrak$', 'youtuberrak', name='youtuberrak'),
    url(r'^idazleak$', 'idazleak', name='idazleak'),
    url(r'^guruak$', 'guruak', name='guruak'),
    url(r'^talde-motorra$', 'talde_motorra', name='talde_motorra'),

    ### EKINTZAK
    url(r'^gehitu-artikulua$', 'add_article', name='add_article'),
    url(r'^gehitu-gameplaya$', 'add_gameplay', name='add_gameplay'),
    url(r'^gehitu-jokoa$', 'add_game', name='add_game'),
    url(r'^gehitu-ekitaldia$', 'add_event', name='add_event'),
    url(r'^gehitu-gustuko-jokoa/(?P<slug>[-\w]+)$', 'add_favorite_game',
       name='gamer_add_favorite_game'),
    url(r'^editatu-profil$', 'edit_profile', name='edit_profile'),
    url(r'^editatu-profil-jakin$', 'edit_notifications', name='edit_profile_noti'),
    url(r'^editatu-profil-ord$', 'edit_computer', name='edit_profile_comp'),
    url(r'^editatu-profil-plat$', 'edit_platform', name='edit_profile_plat'),
    url(r'^editatu-profil-top$', 'edit_top_games', name='edit_profile_top'),
    url(r'^editatu-profil-amaitutakoak$', 'edit_amaitutakoak',
        name='edit_profile_amaitutakoak'),
    url(r'^editatu-profil-pass/$', 'password_change', name='edit_profile_pass'),
    url(r'^editatu-profil-pass-done/$', 'password_change_done',
        name='edit_profile_pass_done'),
    # url(r'^app/', include(router.urls)),

    url(r'^edit-profile-photo$','edit_profile_photo', name='edit_profile_photo'),

    ### HAU BETI AZKENA BEGIRATU BEHAR DA (Ez dauka hitz gakorik)
    url(r'^(?P<username>[-\w]+)$', 'profile', name='gamer_profile'),
)
