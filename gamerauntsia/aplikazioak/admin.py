from gamerauntsia.aplikazioak.models import Aplikazioa
from django.contrib import admin

from datetime import datetime
    
class AplikazioAdmin(admin.ModelAdmin):
    list_display = ('izena','bertsioa','url','slug')
    prepopulated_fields = {"slug": ("izena",)}
   

admin.site.register(Aplikazioa, AplikazioAdmin)
