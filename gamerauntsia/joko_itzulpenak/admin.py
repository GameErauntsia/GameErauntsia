from .models import ItzulpenProiektua, ItzulpenFitxategia, ItzulpenProiektuParteHartzailea, KanpokoItzulpena
from .forms import ItzulpenProiektuaAdminForm
from django.contrib import admin
from django.utils.safestring import mark_safe

class ItzulpenProiektuParteHartzaileaAdminInline(admin.TabularInline):
    model = ItzulpenProiektuParteHartzailea

class ItzulpenFitxategiaAdminInline(admin.TabularInline):
    model = ItzulpenFitxategia
    readonly_fields=['sortze_data']
    ordering=['sortze_data']

class JokoItzulpenaAdmin(admin.ModelAdmin):
    ordering=['sortze_data']
    filter_horizontal = ['plataformak', ]

class ItzulpenProiektuaAdmin(JokoItzulpenaAdmin):
    list_display= ['jokoa','egoera','ofiziala_da','jatorria','preview','sortze_data']
    ordering=['sortze_data']
    list_filter=['egoera','ofiziala_da','jatorria']
    form=ItzulpenProiektuaAdminForm
    fields = ['sortze_data', 'eguneratze_data',
              'erabilgarritasun_data',
              'jokoa','slug','egoera', 'external_url',
              'jatorria','ofiziala_da',
              'arduraduna', 'plataformak',
              'deskribapena','instalazioa', 'ohar_teknikoak']
    filter_horizontal = ['plataformak', ]
    inlines= [ItzulpenProiektuParteHartzaileaAdminInline, ItzulpenFitxategiaAdminInline]

    @mark_safe
    def preview(self, obj):
        return '<a href="/itzulpenak/proiektuak/%s">aurreikusi</a>' % (obj.slug)

class KanpokoItzulpenaAdmin(JokoItzulpenaAdmin):
    list_display= ['jokoa','sortze_data']
    fields = ['jokoa', 'publikoa_da',
              'ofiziala_da','jatorria',
              'erabilgarritasun_data',
              'url','plataformak']

admin.site.register(ItzulpenProiektua, ItzulpenProiektuaAdmin)
admin.site.register(KanpokoItzulpena, KanpokoItzulpenaAdmin)
