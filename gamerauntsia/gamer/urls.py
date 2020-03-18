from django.conf.urls import include, url
from django.contrib.auth import views as authviews
from gamerauntsia.gamer import views

urlpatterns = [
    url(r'^logout$', authviews.LogoutView.as_view(), name='user_logout'),
    url(r'^login$', authviews.LoginView.as_view(), name='user_login'),

    url(r'^$', views.community, name='komunitatea'),
    url(r'^youtuberrak$', views.youtuberrak, name='youtuberrak'),
    url(r'^idazleak$', views.idazleak, name='idazleak'),
    url(r'^guruak$', views.guruak, name='guruak'),
    url(r'^talde-motorra$', views.talde_motorra, name='talde_motorra'),

    # ## BAZKIDETZA
    url(r'^bazkidetza/', include('gamerauntsia.bazkidetza.urls')),

    # ## EKINTZAK
    url(r'^gehitu-artikulua$', views.add_article, name='add_article'),
    url(r'^gehitu-gameplaya$', views.add_gameplay, name='add_gameplay'),
    url(r'^gehitu-jokoa$', views.add_game, name='add_game'),
    url(r'^gehitu-ekitaldia$', views.add_event, name='add_event'),
    url(r'^gehitu-gustuko-jokoa/(?P<slug>[-\w]+)$', views.add_favorite_game, name='gamer_add_favorite_game'),
    url(r'^editatu-profil$', views.edit_profile, name='edit_profile'),
    url(r'^editatu-profil-jakin$', views.edit_notifications, name='edit_profile_noti'),
    url(r'^editatu-profil-argazkia$', views.edit_profile_photo, name='edit_profile_photo'),
    url(r'^editatu-profil-ord$', views.edit_computer, name='edit_profile_comp'),
    url(r'^editatu-profil-plat$', views.edit_platform, name='edit_profile_plat'),
    url(r'^editatu-profil-top$', views.edit_top_games, name='edit_profile_top'),
    url(r'^editatu-profil-amaitutakoak$', views.edit_amaitutakoak, name='edit_profile_amaitutakoak'),
    url(r'^editatu-profil-pass/$', views.password_change, name='edit_profile_pass'),
    url(r'^editatu-profil-pass-done/$', views.password_change_done, name='edit_profile_pass_done'),
    url(r'^edit-profile-photo$', views.edit_profile_photo, name='edit_profile_photo'),

    # ## HAU BETI AZKENA BEGIRATU BEHAR DA (Ez dauka hitz gakorik)
    url(r'^(?P<username>[\w.@+-]+)$', views.profile, name='gamer_profile'),
]
