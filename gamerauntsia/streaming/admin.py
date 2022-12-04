from gamerauntsia.streaming.models import Streaming
from django.contrib import admin


class StreamingAdmin(admin.ModelAdmin):
    list_display = ["twitch_id", "title", "user", "game_name", "start_date", "end_date"]
    fields = ["twitch_id", "title", "user", "game_name", "start_date", "end_date"]
    readonly_fields = ["twitch_id"]
    list_filter = ["user"]
    search_fields = ["title"]
    ordering = ["start_date"]


admin.site.register(Streaming, StreamingAdmin)
