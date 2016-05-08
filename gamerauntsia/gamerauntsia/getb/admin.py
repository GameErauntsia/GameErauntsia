from gamerauntsia.getb.models import Atala
from django.contrib import admin
from django.conf import settings
from gamerauntsia.getb.forms import AtalaAdminForm
from datetime import datetime
from django.utils import timezone

class AtalaAdmin(admin.ModelAdmin):

    def admin_thumbnail(self,obj):
        if obj.argazkia:
            return u'<img src="%s" />' % (obj.argazkia.get_admin_thumbnail_url())
        else:
            return u'(Irudirik ez)'
    admin_thumbnail.short_description = 'Thumb'
    admin_thumbnail.allow_tags = True

    def preview(self,obj):
        return '<a href="/getb/%s">aurreikusi</a>' % (obj.slug)
    preview.allow_tags=True

    list_display = ('admin_thumbnail','izenburua', 'preview','pub_date', 'publikoa_da')
    list_display_links = ('izenburua',)
    prepopulated_fields = {"slug": ("izenburua",)}
    raw_id_fields = ('argazkia',)
    list_filter = ('publikoa_da',)
    search_fields = ['izenburua',]
    ordering = ('-pub_date',)
    form = AtalaAdminForm


admin.site.register(Atala, AtalaAdmin)
