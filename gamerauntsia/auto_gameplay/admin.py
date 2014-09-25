from django.contrib import admin
from gamerauntsia.auto_gameplay.models import AutoGamePlaya
from gamerauntsia.auto_gameplay.forms import AutoGamePlayAdminForm

class GamePlayAdmin(admin.ModelAdmin):
    list_display = ('izenburua', 'slug','zailtasuna', 'jokoa','plataforma', 'erabiltzailea')
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = ('kategoria',)
    raw_id_fields = ('argazkia','jokoa','plataforma','erabiltzailea')
    list_filter = ('erabiltzailea','zailtasuna')
    search_fields = ['erabiltzailea__fullname','erabiltzailea__username','izenburua']
    form = AutoGamePlayAdminForm

    def queryset(self, request):
        qs = super(AutoGamePlayAdmin, self).queryset(request)
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

admin.site.register(AutoGamePlaya, AutoGamePlayAdmin)