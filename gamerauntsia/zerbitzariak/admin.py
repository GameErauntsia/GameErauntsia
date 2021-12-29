from django.contrib import admin
from .models import MC_Whitelist
from gamerauntsia.gamer.models import GamerUser,JokuPlataforma

class MC_WhitelistAdmin(admin.ModelAdmin):
    list_display = ['user','rol','created']
    search_fields = ['user__username',]
    list_filter = ['rol', ]
    ordering = ['-created']

admin.site.register(MC_Whitelist,MC_WhitelistAdmin)
