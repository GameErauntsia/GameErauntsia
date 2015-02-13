from gamerauntsia.gameplaya.models import GamePlaya, Kategoria, Zailtasuna
from django.contrib import admin
from django.conf import settings
from gamerauntsia.gameplaya.forms import GamePlayAdminForm
from datetime import datetime
from django.utils import timezone

class GamePlayAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        if obj.argazkia:
            return u'<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
        else:
            return u'(Irudirik ez)'
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    def preview(self,obj):
        return '<a href="/gameplayak/%s">%s</a>' % (obj.slug, obj.slug)
    preview.allow_tags=True

    list_display = ('izenburua', 'preview','zailtasuna', 'jokoa','plataforma','pub_date', 'erabiltzailea','publikoa_da', 'admin_thumbnail')
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = ('kategoria',)
    raw_id_fields = ('argazkia','jokoa','plataforma','erabiltzailea')
    list_filter = ('erabiltzailea','zailtasuna', 'publikoa_da')
    search_fields = ['erabiltzailea__fullname','erabiltzailea__username','izenburua']
    ordering = ('-pub_date',)
    form = GamePlayAdminForm

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser or (request.user != obj.erabiltzailea and request.user.belongs_group(settings.GP_GROUP)):
            return super(GamePlayAdmin, self).get_readonly_fields(request, obj)
        else:
            return ('status',)

    def queryset(self, request):
        qs = super(GamePlayAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(erabiltzailea = request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser or not request.user.belongs_group(settings.GP_GROUP):
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
