from django.contrib import admin
from django import forms
from gamerauntsia.podcast.models import PodcastShow, PodcastSeason, PodcastEpisode


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


class PodcastEpisodeAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PodcastEpisodeAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PodcastEpisode
        fields = "__all__"


class PodcastEpisodeAdmin(admin.ModelAdmin):
    form = PodcastEpisodeAdminForm
    list_display = ["podcast_season", "name"]
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


admin.site.register(PodcastShow, PodcastShowAdmin)
admin.site.register(PodcastSeason, PodcastSeasonAdmin)
admin.site.register(PodcastEpisode, PodcastEpisodeAdmin)
