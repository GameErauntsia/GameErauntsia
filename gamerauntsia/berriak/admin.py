from gamerauntsia.berriak.models import Berria, Gaia
from django.contrib import admin
from gamerauntsia.berriak.forms import BerriaAdminForm

class BerriakAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        if obj.argazkia:
            return u'<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
        else:
            return u'(Irudirik ez)'
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('izenburua', 'slug', 'erabiltzailea', 'pub_date', 'mod_date', 'publikoa_da','admin_thumbnail')
    prepopulated_fields = {"slug": ("izenburua",)}
    filter_horizontal = ('gaia',)
    list_filter = ('erabiltzailea', 'publikoa_da')
    search_fields = ['erabiltzailea__username','erabiltzailea__fullname','izenburua']
    raw_id_fields = ('argazkia','erabiltzailea')
    ordering = ('-pub_date',)
    form = BerriaAdminForm	

    def queryset(self, request):
        qs = super(BarriakAdmin, self).queryset(request)
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
    

class GaiaAdmin(admin.ModelAdmin):
    list_display = ('izena','slug')
    prepopulated_fields = {"slug": ("izena",)}
    

admin.site.register(Gaia, GaiaAdmin)	
admin.site.register(Berria, BerriakAdmin)
