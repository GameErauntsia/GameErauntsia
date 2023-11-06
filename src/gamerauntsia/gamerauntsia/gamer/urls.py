from django.urls import include, re_path
from django.contrib.auth import views as authviews
from gamerauntsia.gamer import views

urlpatterns = [
    re_path(r"^logout$", authviews.LogoutView.as_view(), name="user_logout"),
    re_path(r"^login$", authviews.LoginView.as_view(), name="user_login"),
    re_path(r"^$", views.community, name="komunitatea"),
    re_path(r"^youtuberrak$", views.youtuberrak, name="youtuberrak"),
    re_path(r"^streamerrak$", views.streamerrak, name="streamerrak"),
    re_path(r"^idazleak$", views.idazleak, name="idazleak"),
    re_path(r"^guruak$", views.guruak, name="guruak"),
    re_path(r"^talde-motorra$", views.talde_motorra, name="talde_motorra"),
    # ## BAZKIDETZA
    re_path(r"^bazkidetza/", include("gamerauntsia.bazkidetza.urls")),
    # ## EKINTZAK
    re_path(r"^gehitu-artikulua$", views.add_article, name="add_article"),
    re_path(r"^gehitu-gameplaya$", views.add_gameplay, name="add_gameplay"),
    re_path(r"^gehitu-jokoa$", views.add_game, name="add_game"),
    re_path(r"^gehitu-ekitaldia$", views.add_event, name="add_event"),
    re_path(
        r"^gehitu-gustuko-jokoa/(?P<slug>[-\w]+)$",
        views.add_favorite_game,
        name="gamer_add_favorite_game",
    ),
    re_path(r"^editatu-profil$", views.edit_profile, name="edit_profile"),
    re_path(r"^editatu-profil-jakin$", views.edit_notifications, name="edit_profile_noti"),
    re_path(
        r"^editatu-profil-argazkia$",
        views.edit_profile_photo,
        name="edit_profile_photo",
    ),
    re_path(r"^editatu-profil-ord$", views.edit_computer, name="edit_profile_comp"),
    re_path(r"^editatu-profil-plat$", views.edit_platform, name="edit_profile_plat"),
    re_path(r"^editatu-profil-top$", views.edit_top_games, name="edit_profile_top"),
    re_path(
        r"^editatu-profil-amaitutakoak$",
        views.edit_amaitutakoak,
        name="edit_profile_amaitutakoak",
    ),
    re_path(r"^editatu-profil-pass/$", views.password_change, name="edit_profile_pass"),
    re_path(
        r"^editatu-profil-pass-done/$",
        views.password_change_done,
        name="edit_profile_pass_done",
    ),
    re_path(r"^edit-profile-photo$", views.edit_profile_photo, name="edit_profile_photo"),
    re_path(r"^editatu-profil-kanalak", views.edit_channels, name="edit_profile_kanalak"),
    # ## HAU BETI AZKENA BEGIRATU BEHAR DA (Ez dauka hitz gakorik)
    re_path(r"^(?P<username>[\w.@+-]+)$", views.profile, name="gamer_profile"),
]
