from django.contrib import admin
from gamerauntsia.txapelketak.models import Txapelketa, Partida, Partaidea
from gamerauntsia.gamer.models import GamerUser
from forms import PartidaInlineForm, TxapelketaAdminForm
from mptt.admin import MPTTModelAdmin

class PartidaAdmin(MPTTModelAdmin):

    def get_partaideak(self, obj):
        return " VS ".join([p.get_izena() for p in obj.partaideak.all()])

    list_display = ('txapelketa', 'jardunaldia','get_partaideak','emaitza', 'date')
    filter_horizontal = ('partaideak',)
    raw_id_fields = ('parent','txapelketa','gameplaya')
    search_fields = ['txapelketa__izena']
    ordering = ('-date',)



class PartidaInline(admin.TabularInline):
    model = Partida
    fields = ('jardunaldia','partaideak','emaitza','parent','date')
    form = PartidaInlineForm

class TxapelketaAdmin(admin.ModelAdmin):
    list_display = ('izena', 'slug','mota', 'modalitatea','jokoa','insk_date','pub_date', 'status', 'publikoa_da')
    prepopulated_fields = {"slug": ("izena",)}
    filter_horizontal = ('jokalariak',)
    raw_id_fields = ('irudia','jokoa')
    list_filter = ('mota','modalitatea', 'publikoa_da')
    search_fields = ['izena','slug']
    ordering = ('-pub_date',)
    form = TxapelketaAdminForm
    inlines = [PartidaInline]

class PartaideakAdmin(admin.ModelAdmin):

    def get_izena(self, obj):
        if not obj.izena:
            if len(obj.jokalariak.all()) == 1:
                return obj.jokalariak.all()[0].username
            else:
                return ", ".join([p.username for p in obj.jokalariak.all()])
        return obj.izena

    list_display = ('txapelketa', 'get_izena', 'win','lose', 'points')
    filter_horizontal = ('jokalariak',)
    raw_id_fields = ('irudia',)
    search_fields = ['izena']
    ordering = ('-id',)

admin.site.register(Txapelketa,TxapelketaAdmin)
admin.site.register(Partida,PartidaAdmin)
admin.site.register(Partaidea,PartaideakAdmin)