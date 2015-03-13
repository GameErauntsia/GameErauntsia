from gamerauntsia.jokoa.models import Jokoa, Plataforma
from django.contrib import admin

from datetime import datetime
    
class JokoaAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        if obj.logoa:
            return u'<img src="%s" />' % obj.logoa.get_admin_thumbnail_url()
        else:
            return '(Irudirik ez)'
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('izena','bertsioa','url','slug', 'admin_thumbnail' )
    prepopulated_fields = {"slug": ("izena","bertsioa")}
    search_fields = ['izena',]
    ordering = ('izena','bertsioa')

    fieldsets = (
        ('Datu orokorrak',
        {'fields':('izena','bertsioa','slug', 'desk')},),
        ('Osagarriak',
        {'fields':('lizentzia','url', 'logoa', 'wiki')},),
    )

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('izena',)
    prepopulated_fields = {"slug": ("izena",)}
    ordering = ('izena',)
   

admin.site.register(Jokoa, JokoaAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
