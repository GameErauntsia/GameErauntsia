from .models import Bazkidea, Eskaintza, Eskaera, OparitzekoJokoak
from django.contrib import admin
from .forms import EskaintzaAdminForm
from django.utils.safestring import mark_safe

class BazkideaAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'paid', 'is_active', 'expire_date', 'date_joined']
    search_fields = ['id','user']
    raw_id_fields = ['user', ]
    ordering = ['-id', ]


class EskaintzaAdmin(admin.ModelAdmin):

    @mark_safe
    def admin_thumbnail(self,obj):
        try:
            if obj.irudia:
                return u'<img src="%s" />' % (obj.irudia.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.irudia.title)
    admin_thumbnail.short_description = 'Thumb'

    list_display = ['admin_thumbnail', 'izena', 'mota', 'expire_date', 'activate_date', 'is_public']
    list_display_links = ['admin_thumbnail', 'izena']
    search_fields = ['izena','deskribapena']
    raw_id_fields = ['irudia', ]
    prepopulated_fields = {"slug": ("izena",)}
    ordering = ['-expire_date','activate_date']
    form = EskaintzaAdminForm

class EskaeraAdmin(admin.ModelAdmin):
    list_display = ['added', 'eskaintza', 'bazkidea', 'is_active']
    search_fields = ['eskaintza','bazkidea']
    raw_id_fields = ['eskaintza', 'bazkidea']
    ordering = ['-added', ]

class OparitzekoJokoakAdmin(admin.ModelAdmin):
    list_display = ['key','jokoa', 'plataforma', 'non_aldatzeko', 'oparituta',   'pub_date']
    search_fields = ['jokoa__izena', ]
    list_filter = ['plataforma', 'oparituta']
    raw_id_fields = ['jokoa', ]
    ordering = ['-pub_date', ]

admin.site.register(Bazkidea, BazkideaAdmin)
admin.site.register(Eskaintza, EskaintzaAdmin)
admin.site.register(Eskaera, EskaeraAdmin)
admin.site.register(OparitzekoJokoak, OparitzekoJokoakAdmin)
