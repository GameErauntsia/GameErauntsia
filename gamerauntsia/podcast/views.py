from django.shortcuts import render, get_object_or_404
from gamerauntsia.podcast.models import PodcastShow, PodcastEpisode


def index(request):
    podcast_shows = PodcastShow.objects.filter(is_public=True).select_related("image")
    return render(request, "podcast/index.html", locals())


def show(request, show_slug):
    show = get_object_or_404(
        PodcastShow.objects.select_related("image"), slug=show_slug
    )
    show_episodes = PodcastEpisode.objects.filter(
        is_public=True, podcast_season__podcast_show=show
    ).order_by("-podcast_season__number", "-number")
    return render(request, "podcast/show.html", locals())


def episode(request, show_slug, episode_slug):
    episode = get_object_or_404(
        PodcastEpisode.objects.select_related(
            "image", "podcast_season", "podcast_season__podcast_show"
        ),
        podcast_season__podcast_show__slug=show_slug,
        slug=episode_slug,
        is_public=True,
    )
    audios = episode.podcastepisodeaudioplatform_set.all().order_by(
        "-audio_platform__priority"
    )
    videos = episode.podcastepisodevideoplatform_set.all().order_by(
        "-video_platform__priority"
    )
    return render(request, "podcast/episode.html", locals())
