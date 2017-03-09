from models import Terminoa
from django.contrib import admin


class TerminoaAdmin(admin.ModelAdmin):
    list_display = ['term_eu','term_es','term_en','jokoa']
    search_fields = ['term_eu','term_es','term_en']
    raw_id_fields = ['jokoa', ]
    ordering = ['term_eu', ]


admin.site.register(Terminoa, TerminoaAdmin)

from photologue.admin import PhotoAdmin
from photologue.models import Photo

class PhotoAdmin2(PhotoAdmin):
    def getphotoadmin(self, obj):
        """ """
        try:
            return u'<img src="%s" />' % obj.get_admin_thumbnail_url()
        except:
            return '%s' % (obj.title)
    getphotoadmin.allow_tags = True
    getphotoadmin.short_description = 'Irudia'

    list_display = ['getphotoadmin', 'title', 'date_added', 'is_public']

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin2)
