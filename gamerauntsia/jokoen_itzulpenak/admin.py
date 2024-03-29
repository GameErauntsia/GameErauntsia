from django.contrib import admin
from .models import Itzulpena, EuskarazkoJokoa, Euskalinkak
from .forms import EuskarazkoJokoaAdminForm
from django.utils.safestring import mark_safe


class ItzulpenakAdmin(admin.ModelAdmin):
    list_display = ["izena", "pub_date", "mod_date", "status", "publikoa_da"]
    list_display_links = ["izena"]
    list_filter = ["publikoa_da", "status"]
    search_fields = [
        "izena",
    ]
    ordering = [
        "-pub_date",
    ]


class EuskarazkoJokoaAdmin(admin.ModelAdmin):
    @mark_safe
    def admin_thumbnail(self, obj):
        try:
            if obj.jokoa and obj.jokoa.logoa:
                return '<img src="%s" />' % (obj.jokoa.logoa.get_admin_thumbnail_url())
            else:
                return "(Irudirik ez)"
        except:
            return "%s" % (obj.jokoa.logoa.title)

    admin_thumbnail.short_description = "Thumb"

    def get_plataformak(self, obj):
        return ", ".join([plat.izena for plat in obj.plataformak.all()])

    list_display = [
        "admin_thumbnail",
        "jokoa",
        "get_plataformak",
        "pub_date",
        "is_ge_translation",
        "publikoa_da",
    ]
    list_display_links = ["admin_thumbnail", "jokoa"]
    list_filter = ["publikoa_da", "plataformak"]
    filter_horizontal = [
        "plataformak",
    ]
    search_fields = [
        "jokoa__izena",
    ]
    raw_id_fields = [
        "jokoa",
    ]
    ordering = [
        "-pub_date",
    ]
    form = EuskarazkoJokoaAdminForm


class EuskalinkakAdmin(admin.ModelAdmin):
    @mark_safe
    def admin_thumbnail(self, obj):
        try:
            if obj.irudia:
                return '<img src="%s" />' % (obj.irudia.get_admin_thumbnail_url())
            else:
                return "(Irudirik ez)"
        except:
            return "%s" % (obj.irudia.title)

    admin_thumbnail.short_description = "Logoa"

    list_display = ["admin_thumbnail", "izena", "url", "pub_date", "publikoa_da"]
    list_display_links = ["admin_thumbnail", "izena"]
    list_filter = [
        "publikoa_da",
    ]
    search_fields = [
        "izena",
    ]
    ordering = [
        "-pub_date",
    ]


admin.site.register(Itzulpena, ItzulpenakAdmin)
admin.site.register(EuskarazkoJokoa, EuskarazkoJokoaAdmin)
admin.site.register(Euskalinkak, EuskalinkakAdmin)
