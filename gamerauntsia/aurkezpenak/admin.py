from django.contrib import admin
from gamerauntsia.aurkezpenak.models import Aurkezpena
from gamerauntsia.aurkezpenak.forms import AurkezpenaAdminForm


class AurkezpenaAdmin(admin.ModelAdmin):
    list_display = ["izena", "slug", "erabiltzailea"]
    prepopulated_fields = {"slug": ("izena",)}
    list_filter = [
        "izena",
    ]
    search_fields = [
        "izena",
        "slug",
    ]
    # form = AurkezpenaAdminForm


admin.site.register(Aurkezpena, AurkezpenaAdmin)
