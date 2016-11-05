from django.contrib import admin
from models import Itzulpena, EuskarazkoJokoa, Euskalinkak

class ItzulpenakAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        try:
            if obj.jokoa and obj.jokoa.logoa:
                return u'<img src="%s" />' % (obj.jokoa.logoa.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.jokoa.logoa.title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('admin_thumbnail', 'izena', 'jokoa', 'plataforma', 'pub_date', 'mod_date','status','publikoa_da')
    list_display_links = ('admin_thumbnail', 'izena',)
    list_filter = ('publikoa_da', 'status', 'plataforma')
    search_fields = ['izena','jokoa__izena']
    ordering = ('-pub_date',)


class EuskarazkoJokoaAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        try:
            if obj.jokoa and obj.jokoa.logoa:
                return u'<img src="%s" />' % (obj.jokoa.logoa.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.jokoa.logoa.title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('admin_thumbnail', 'jokoa', 'plataforma', 'pub_date', 'publikoa_da')
    list_display_links = ('admin_thumbnail', 'jokoa',)
    list_filter = ('publikoa_da', 'plataforma')
    search_fields = ['jokoa__izena', ]
    ordering = ('-pub_date',)


class EuskalinkakAdmin(admin.ModelAdmin):
    def admin_thumbnail(self,obj):
        try:
            if obj.irudia:
                return u'<img src="%s" />' % (obj.irudia.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.irudia.title)
    admin_thumbnail.short_description = 'Logoa'
    admin_thumbnail.allow_tags = True

    list_display = ('admin_thumbnail', 'izena', 'url', 'pub_date', 'publikoa_da')
    list_display_links = ('admin_thumbnail', 'izena',)
    list_filter = ('publikoa_da',)
    search_fields = ['izena', ]
    ordering = ('-pub_date',)

admin.site.register(Itzulpena, ItzulpenakAdmin)
admin.site.register(EuskarazkoJokoa, EuskarazkoJokoaAdmin)
admin.site.register(Euskalinkak, EuskalinkakAdmin)