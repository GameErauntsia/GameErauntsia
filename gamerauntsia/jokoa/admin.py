from gamerauntsia.jokoa.models import Jokoa
from django.contrib import admin

from datetime import datetime
    
class JokoaAdmin(admin.ModelAdmin):
    list_display = ('izena','bertsioa','url','slug')
    prepopulated_fields = {"slug": ("izena","bertsioa")}

    fieldsets = (
        ('Datu orokorrak',
        {'fields':('izena','bertsioa','slug', 'desk')},),
        ('Osagarriak',
        {'fields':('lizentzia','url', 'logoa', 'wiki')},),
    )
   

admin.site.register(Jokoa, JokoaAdmin)
