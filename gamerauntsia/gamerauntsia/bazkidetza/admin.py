from models import Bazkidea
from django.contrib import admin


class BazkideaAdmin(admin.ModelAdmin):
    list_display = ('id','user','paid','is_active', 'expire_date', 'date_joined')
    search_fields = ['id','user']
    raw_id_fields = ('user',)
    ordering = ('-id',)


admin.site.register(Bazkidea, BazkideaAdmin)
