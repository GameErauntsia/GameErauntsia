from .models import Terminoa
from django.contrib import admin
from gamerauntsia.base.forms import FlatPageForm
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django.utils.safestring import mark_safe


class TerminoaAdmin(admin.ModelAdmin):
    list_display = ['term_eu','term_es','term_en']
    search_fields = ['term_eu','term_es','term_en']
    filter_horizontal = ['jokoak', ]
    ordering = ['term_eu', ]


admin.site.register(Terminoa, TerminoaAdmin)

from photologue.admin import PhotoAdmin
from photologue.models import Photo

class PhotoAdmin2(PhotoAdmin):

    @mark_safe
    def getphotoadmin(self, obj):
        """ """
        try:
            return u'<img src="%s" />' % obj.get_admin_thumbnail_url()
        except:
            return '%s' % (obj.title)
    getphotoadmin.short_description = 'Irudia'

    list_display = ['getphotoadmin', 'title', 'date_added', 'is_public']

admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin2)


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageForm
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)