from django.contrib import admin
from models import Itzulpena 

class ItzulpenakAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        try:
            if obj.jokoa and obj.jokoa.logoa:
                return u'<img src="%s" />' % (obj.jokoa.logoa.get_admin_thumbnail_url())
            else:
                return u'(Irudirik ez)'
        except:
            return '%s' % (obj.jokoa.logoa.title)
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    list_display = ('admin_thumbnail', 'izena', 'jokoa', 'plataforma', 'pub_date', 'mod_date','status','publikoa_da')
    list_display_links = ('izena',)
    list_filter = ('publikoa_da', 'status')
    search_fields = ['izena','jokoa__izena']
    ordering = ('-pub_date',)

admin.site.register(Itzulpena, ItzulpenakAdmin)