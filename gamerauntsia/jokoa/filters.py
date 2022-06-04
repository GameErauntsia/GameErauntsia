import django_filters
from gamerauntsia.jokoa.models import Jokoa, Plataforma
from gamerauntsia.joko_itzulpenak.models import ITZULPEN_JATORRIAK

BOOLEAN_CHOICES = (
    (True, 'Bai'),
    (False, 'Ez'),
)

class EuskarazkoJokoaFilter(django_filters.FilterSet):
    izena = django_filters.CharFilter(lookup_expr='icontains',
                                      label="Bilatu izenez")
    plataformak = django_filters.ModelMultipleChoiceFilter(field_name='jokoitzulpena__plataformak',
                                                           queryset=Plataforma.objects,
                                                           label="Plataformak")
    ofiziala_da = django_filters.ChoiceFilter(field_name='jokoitzulpena__ofiziala_da',
                                              choices=BOOLEAN_CHOICES,
                                              label="Ofiziala",
                                              empty_label="-")
    jatorria = django_filters.ChoiceFilter(field_name='jokoitzulpena__jatorria',
                                           choices=ITZULPEN_JATORRIAK,
                                           label="Mota",
                                           empty_label="-")

    ordena = django_filters.OrderingFilter(fields=(('izena','izena'),
                                                   ('argitaratze_data','argitaratze_data')),
                                           choices=(('izena', 'Izena (a-z)'),
                                                    ('-izena', 'Izena (z-a)'),
                                                    ('-argitaratze_data','Argitaratze data (berrienak lehenengo)'),
                                                    ('argitaratze_data','Argitaratze data (zaharrenak lehenengo)'),
                                                    ('-jokoitzulpena__erabilgarritasun_data','Euskaratze data (berrienak lehenengo)'),
                                                    ('jokoitzulpena__erabilgarritasun_data','Euskaratze data (zaharrenak lehenengo)'),
                                                    ),
                                           empty_label="-")
    class Meta:
        model = Jokoa
        fields= ['izena']
