from gamerauntsia.gameplaya.models import GamePlaya, Kategoria, Zailtasuna
from django.contrib import admin
from gamerauntsia.gameplaya.forms import GamePlayAdminForm

from datetime import datetime
from django.utils import timezone

class GamePlayAdmin(admin.ModelAdmin):
    list_display = ('izenburua', 'slug','zailtasuna', 'jokoa','pub_date', 'erabiltzailea','publikoa_da')
    prepopulated_fields = {"slug": ("izenburua",)}
    form = GamePlayAdminForm
    row_fields = ('argazkia','erabiltzailea')
    
class GaiaAdmin(admin.ModelAdmin):
    list_display = ('izena','slug')
    prepopulated_fields = {"slug": ("izena",)}
    
class ZailtasunAdmin(admin.ModelAdmin):
    list_display = ('izena',)
    prepopulated_fields = {"slug": ("izena",)}

admin.site.register(GamePlaya, GamePlayAdmin)
admin.site.register(Kategoria, GaiaAdmin)
admin.site.register(Zailtasuna, ZailtasunAdmin)
