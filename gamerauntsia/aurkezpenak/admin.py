from django.contrib import admin
from gamerauntsia.aurkezpenak.models import Aurkezpena

class AurkezpenaAdmin(admin.ModelAdmin):
    list_display = ('izena', 'slug','template_name')
    prepopulated_fields = {"slug": ("izena",)}
    list_filter = ('izena',)
    search_fields = ['izena','template_name',]

admin.site.register(Aurkezpena, AurkezpenaAdmin)