from models import Terminoa
from django.contrib import admin


class TerminoaAdmin(admin.ModelAdmin):
    list_display = ('term_eu','term_es','term_en')
    ordering = ('term_eu',)
   

admin.site.register(Terminoa, TerminoaAdmin)