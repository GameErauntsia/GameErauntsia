from django.urls import re_path
from gamerauntsia.podcast import views

urlpatterns = [
    re_path(r"^$", views.index, name="podcast_index"),
    re_path(r"^(?P<show_slug>[-\w]+)$", views.show, name="podcast_show"),
    re_path(
        r"^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)",
        views.episode,
        name="podcast_episode",
    ),
]
