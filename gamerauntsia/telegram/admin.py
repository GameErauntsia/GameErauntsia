from django.contrib import admin
from .models import TelegramGroup


class TelegramAdmin(admin.ModelAdmin):
    list_display = [
        "izena",
    ]
    ordering = [
        "izena",
    ]


admin.site.register(TelegramGroup, TelegramAdmin)
