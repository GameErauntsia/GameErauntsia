from gamerauntsia.getb.models import Atala
from django.contrib import admin
from django.conf import settings
from gamerauntsia.getb.forms import AtalaAdminForm
from datetime import datetime
from django.utils import timezone
from django.utils.safestring import mark_safe

class AtalaAdmin(admin.ModelAdmin):

    @mark_safe
    def admin_thumbnail(self,obj):
        if obj.argazkia:
            return u'<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
        else:
            return u'(Irudirik ez)'
    admin_thumbnail.short_description = 'Thumb'
    
    @mark_safe
    def preview(self,obj):
        return '<a href="/getb/%s">aurreikusi</a>' % (obj.slug)

    list_display = ['admin_thumbnail','izenburua', 'preview','pub_date', 'publikoa_da']
    list_display_links = ['izenburua', ]
    prepopulated_fields = {"slug": ("izenburua",)}
    raw_id_fields = ['argazkia', ]
    list_filter = ['publikoa_da', ]
    search_fields = ['izenburua', ]
    ordering = ['-pub_date', ]
    form = AtalaAdminForm


admin.site.register(Atala, AtalaAdmin)
