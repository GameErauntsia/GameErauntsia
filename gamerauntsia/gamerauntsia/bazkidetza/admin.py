from models import Bazkidea, Eskaintza
from django.contrib import admin
from forms import EskaintzaAdminForm

class BazkideaAdmin(admin.ModelAdmin):
    list_display = ('id','user','paid','is_active', 'expire_date', 'date_joined')
    search_fields = ['id','user']
    raw_id_fields = ('user',)
    ordering = ('-id',)


class EskaintzaAdmin(admin.ModelAdmin):
    def admin_thumbnail(self,obj):
        try:
            if obj.irudia:
                return u'<img src="%s" />' % (obj.irudia.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.irudia.title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('admin_thumbnail', 'izena', 'mota', 'expire_date', 'activate_date', 'is_public')
    search_fields = ['izena','deskribapena']
    raw_id_fields = ('irudia',)
    prepopulated_fields = {"slug": ("izena",)}
    ordering = ('-expire_date','activate_date')
    form = EskaintzaAdminForm


admin.site.register(Bazkidea, BazkideaAdmin)
admin.site.register(Eskaintza, EskaintzaAdmin)
