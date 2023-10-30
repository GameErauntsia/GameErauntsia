from gamerauntsia.berriak.models import Berria, Gaia
from django.contrib import admin
from django.conf import settings
from gamerauntsia.berriak.forms import BerriaAdminForm
from django.utils.safestring import mark_safe


class BerriakAdmin(admin.ModelAdmin):
    @mark_safe
    def admin_thumbnail(self, obj):
        try:
            if obj.argazkia:
                return '<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
            else:
                return "(Irudirik ez)"
        except:
            return "%s" % (obj.argazkia.title)

    admin_thumbnail.short_description = "Thumb"

    @mark_safe
    def preview(self, obj):
        return '<a href="/bloga/%s">aurreikusi</a>' % (obj.slug)

    list_display = [
        "admin_thumbnail",
        "izenburua",
        "preview",
        "erabiltzailea",
        "pub_date",
        "mod_date",
        "publikoa_da",
        "status",
        "shared",
    ]
    list_display_links = [
        "izenburua",
    ]
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = [
        "gaia",
    ]
    list_filter = ("publikoa_da", "status")
    search_fields = ["erabiltzailea__username", "erabiltzailea__fullname", "izenburua"]
    raw_id_fields = ["argazkia", "erabiltzailea", "jokoa"]
    ordering = [
        "-pub_date",
    ]
    form = BerriaAdminForm

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser or (
            obj
            and request.user != obj.erabiltzailea
            and request.user.belongs_group(settings.NEWS_GROUP)
        ):
            return super(BerriakAdmin, self).get_readonly_fields(request, obj)
        else:
            return "status"

    def queryset(self, request):
        qs = super(BerriakAdmin, self).queryset(request)
        if request.user.is_superuser or request.user.belongs_group(settings.NEWS_GROUP):
            return qs
        else:
            return qs.filter(erabiltzailea=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True  # So they can see the change list page
        if (
            request.user.is_superuser
            or obj.erabiltzailea == request.user
            or request.user.belongs_group(settings.NEWS_GROUP)
        ):
            return True
        else:
            return False

    has_delete_permission = has_change_permission


class GaiaAdmin(admin.ModelAdmin):
    list_display = ["izena", "slug"]
    prepopulated_fields = {"slug": ("izena",)}


admin.site.register(Gaia, GaiaAdmin)
admin.site.register(Berria, BerriakAdmin)
