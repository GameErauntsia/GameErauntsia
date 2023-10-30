from django.conf.urls import url
from gamerauntsia.podcast import views

urlpatterns = [
    url(r"^$", views.index, name="podcast_index"),
    url(r"^(?P<show_slug>[-\w]+)$", views.show, name="podcast_show"),
    url(
        r"^(?P<show_slug>[-\w]+)/(?P<episode_slug>[-\w]+)",
        views.episode,
        name="podcast_episode",
    ),
]
