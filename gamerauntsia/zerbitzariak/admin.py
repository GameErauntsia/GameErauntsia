from django.contrib import admin
from models import *

class MC_WhitelistAdmin(admin.ModelAdmin):
    list_display = ('mc_user','uuid','user','rol','created')
    ordering = ('-created',)

admin.site.register(MC_Whitelist,MC_WhitelistAdmin)
