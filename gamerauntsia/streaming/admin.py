from gamerauntsia.streaming.models import Streaming
from django.contrib import admin

class StreamingAdmin(admin.ModelAdmin):
    list_display= ['title']

admin.site.register(Streaming, StreamingAdmin)
