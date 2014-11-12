from gamerauntsia.gameplaya.models import GamePlaya, Kategoria, Zailtasuna
from django.contrib import admin
from gamerauntsia.gameplaya.forms import GamePlayAdminForm
from datetime import datetime
from django.utils import timezone

class GamePlayAdmin(admin.ModelAdmin):

    def image_tag(self,obj):
        if obj.argazkia:
            return u'<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
        else:
            return u'(Irudirik ez)'
        image_tag.allow_tags = True

    list_display = ('izenburua', 'slug','zailtasuna', 'jokoa','plataforma','pub_date', 'erabiltzailea','publikoa_da', 'image_tag')
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = ('kategoria',)
    raw_id_fields = ('argazkia','jokoa','plataforma','erabiltzailea')
    list_filter = ('erabiltzailea','zailtasuna', 'publikoa_da')
    search_fields = ['erabiltzailea__fullname','erabiltzailea__username','izenburua']
    ordering = ('-pub_date',)
    form = GamePlayAdminForm

    def queryset(self, request):
        qs = super(GamePlayAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(erabiltzailea = request.user)
    
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.erabiltzailea = request.user
        obj.save()
    
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True # So they can see the change list page
        if request.user.is_superuser or obj.erabiltzailea == request.user:
            return True
        else:
            return False
    
    has_delete_permission = has_change_permission
    
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ('izena','slug')
    prepopulated_fields = {"slug": ("izena",)}
    
class ZailtasunAdmin(admin.ModelAdmin):
    list_display = ('izena',)
    prepopulated_fields = {"slug": ("izena",)}

admin.site.register(GamePlaya, GamePlayAdmin)
admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Zailtasuna, ZailtasunAdmin)
