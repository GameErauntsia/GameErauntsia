from gamerauntsia.jokoa.models import Jokoa, Plataforma
from django.contrib import admin

from datetime import datetime
    
class JokoaAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        try:
            if obj.logoa:
                return u'<img src="%s" />' % (obj.logoa.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.logoa.title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    def preview(self,obj):
        return '<a href="/jokoak/%s">aurreikusi</a>' % (obj.slug)
    preview.allow_tags=True

    list_display = ('admin_thumbnail','izena','bertsioa','preview','url','slug','steam_id', 'publikoa_da' )
    list_display_links = ('izena',)
    prepopulated_fields = {"slug": ("izena","bertsioa")}
    search_fields = ['izena',]
    ordering = ('izena','bertsioa')

    fieldsets = (
        ('Datu orokorrak',
        {'fields':('izena','bertsioa','slug', 'desk', 'lizentzia','url', 'logoa', 'publikoa_da')},),
        ('Osagarriak',
        {'fields':('steam_id','trailer', 'wiki')},),
    )

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('izena',)
    prepopulated_fields = {"slug": ("izena",)}
    ordering = ('izena',)
   

admin.site.register(Jokoa, JokoaAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
