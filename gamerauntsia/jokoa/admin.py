from gamerauntsia.jokoa.models import Jokoa, Plataforma, Garatzailea, Generoa
from django.contrib import admin
from django.utils.safestring import mark_safe

from datetime import datetime


class JokoaAdmin(admin.ModelAdmin):
    @mark_safe
    def admin_thumbnail(self, obj):
        try:
            if obj.logoa:
                return '<img src="%s" />' % (obj.logoa.get_admin_thumbnail_url())
            else:
                return "(Irudirik ez)"
        except:
            return "%s" % (obj.logoa.title)

    admin_thumbnail.short_description = "Thumb"

    @mark_safe
    def preview(self, obj):
        return '<a href="/jokoak/%s">aurreikusi</a>' % (obj.slug)

    preview.allow_tags = True

    list_display = [
        "admin_thumbnail",
        "izena",
        "bertsioa",
        "preview",
        "url",
        "slug",
        "steam_id",
        "publikoa_da",
    ]
    list_display_links = [
        "izena",
    ]
    prepopulated_fields = {"slug": ("izena", "bertsioa")}
    list_filter = [
        "publikoa_da",
    ]
    search_fields = ["izena", "bertsioa"]
    ordering = ["izena", "bertsioa"]
    filter_horizontal = [
        "generoak",
    ]
    raw_id_fields = ["logoa", "karatula", "garatzailea"]
    fieldsets = (
        (
            "Datu orokorrak",
            {
                "fields": (
                    "izena",
                    "bertsioa",
                    "slug",
                    "desk",
                    "lizentzia",
                    "garatzailea",
                    "generoak",
                    "url",
                    "logoa",
                    "karatula",
                    "publikoa_da",
                )
            },
        ),
        (
            "Osagarriak",
            {"fields": ("argitaratze_data", "steam_id", "trailer", "wiki")},
        ),
    )


class PlataformaAdmin(admin.ModelAdmin):
    list_display = [
        "izena",
    ]
    prepopulated_fields = {"slug": ("izena",)}
    ordering = [
        "izena",
    ]


class GeneroaAdmin(admin.ModelAdmin):
    list_display = [
        "izena",
    ]
    prepopulated_fields = {"slug": ("izena",)}
    ordering = [
        "izena",
    ]


class GaratzaileaAdmin(admin.ModelAdmin):
    list_display = [
        "izena",
    ]
    prepopulated_fields = {"slug": ("izena",)}
    ordering = [
        "izena",
    ]


admin.site.register(Jokoa, JokoaAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Generoa, GeneroaAdmin)
admin.site.register(Garatzailea, GaratzaileaAdmin)
