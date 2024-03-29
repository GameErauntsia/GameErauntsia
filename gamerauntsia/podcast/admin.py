from django.contrib import admin
from django import forms
from gamerauntsia.podcast.models import (
    PodcastShow,
    PodcastSeason,
    PodcastEpisode,
    PodcastVideoPlatform,
    PodcastAudioPlatform,
    PodcastEpisodeVideoPlatform,
    PodcastEpisodeAudioPlatform,
)


class PodcastVideoPlatformAdmin(admin.ModelAdmin):
    list_display = ["name", "priority"]


class PodcastAudioPlatformAdmin(admin.ModelAdmin):
    list_display = ["name", "priority"]


class PodcastShowAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PodcastShowAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PodcastShow
        fields = "__all__"


class PodcastShowAdmin(admin.ModelAdmin):
    form = PodcastShowAdminForm
    list_display = ["name"]
    fields = ["name", "slug", "status", "is_public", "image", "description"]
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ["image"]


class PodcastSeasonAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PodcastSeasonAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PodcastSeason
        fields = "__all__"


class PodcastSeasonAdmin(admin.ModelAdmin):
    form = PodcastSeasonAdminForm
    list_display = ["podcast_show", "name"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["podcast_show"]


class PodcastEpisodeAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PodcastEpisodeAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PodcastEpisode
        fields = "__all__"


class PodcastEpisodeVideoPlatformAdminInline(admin.TabularInline):
    model = PodcastEpisodeVideoPlatform


class PodcastEpisodeAudioPlatformAdminInline(admin.TabularInline):
    model = PodcastEpisodeAudioPlatform


class PodcastEpisodeAdmin(admin.ModelAdmin):
    form = PodcastEpisodeAdminForm
    list_display = ["podcast_season", "number", "name"]
    fields = [
        "podcast_season",
        "number",
        "name",
        "slug",
        "image",
        "description",
        "is_public",
        "pub_date",
    ]
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ["image"]
    ordering = ["pub_date"]
    list_filter = ["podcast_season__podcast_show", "podcast_season"]
    inlines = [
        PodcastEpisodeVideoPlatformAdminInline,
        PodcastEpisodeAudioPlatformAdminInline,
    ]


admin.site.register(PodcastShow, PodcastShowAdmin)
admin.site.register(PodcastSeason, PodcastSeasonAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
admin.site.register(PodcastVideoPlatform, PodcastVideoPlatformAdmin)
admin.site.register(PodcastAudioPlatform, PodcastAudioPlatformAdmin)
