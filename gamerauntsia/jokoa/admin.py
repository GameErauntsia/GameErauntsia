from gamerauntsia.jokoa.models import Jokoa
from django.contrib import admin

from datetime import datetime
    
class JokoaAdmin(admin.ModelAdmin):
    list_display = ('izena','bertsioa','url','slug')
    prepopulated_fields = {"slug": ("izena",)}
   

admin.site.register(Jokoa, JokoaAdmin)
