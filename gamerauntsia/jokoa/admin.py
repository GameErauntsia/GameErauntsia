from gamerauntsia.jokoa.models import Jokoa, Plataforma
from django.contrib import admin

from datetime import datetime
    
class JokoaAdmin(admin.ModelAdmin):
    list_display = ('izena','bertsioa','url','slug')
    prepopulated_fields = {"slug": ("izena","bertsioa")}
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
