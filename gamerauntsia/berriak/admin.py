from gamerauntsia.berriak.models import Berria, Gaia
from django.contrib import admin
from gamerauntsia.berriak.forms import BerriaAdminForm

class BarriakAdmin(admin.ModelAdmin):
    list_display = ('izenburua', 'slug', 'erabiltzailea', 'pub_date', 'mod_date', 'publikoa_da')
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = ('gaia',)
    list_filter = ('erabiltzailea', 'publikoa_da')
    search_fields = ['erabiltzailea','izenburua']
    form = BerriaAdminForm	
    

class GaiaAdmin(admin.ModelAdmin):
    list_display = ('izena','slug')
    prepopulated_fields = {"slug": ("izena",)}
    

admin.site.register(Gaia, GaiaAdmin)	
admin.site.register(Berria, BarriakAdmin)
