from .models import ItzulpenProiektua, ItzulpenFitxategia, ItzulpenProiektuParteHartzailea, KanpokoItzulpena
from .forms import ItzulpenProiektuaAdminForm
from django.contrib import admin

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
    list_display= ['jokoa','egoera','sortze_data']
    ordering=['sortze_data']
    list_filter=['egoera']
    form=ItzulpenProiektuaAdminForm
    fields = ['sortze_data', 'eguneratze_data',
              'erabilgarritasun_data',
              'jokoa','slug','egoera', 'url',
              'jatorria','ofiziala_da',
              'arduraduna', 'plataformak',
              'deskribapena','instalazioa', 'ohar_teknikoak']
    filter_horizontal = ['plataformak', ]
    inlines= [ItzulpenProiektuParteHartzaileaAdminInline, ItzulpenFitxategiaAdminInline]

class KanpokoItzulpenaAdmin(JokoItzulpenaAdmin):
    list_display= ['jokoa','sortze_data']
    fields = ['jokoa', 'publikoa_da',
              'erabilgarritasun_data',
              'url','plataformak']

admin.site.register(ItzulpenProiektua, ItzulpenProiektuaAdmin)
admin.site.register(KanpokoItzulpena, KanpokoItzulpenaAdmin)
