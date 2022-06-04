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
    # argitaratze_data = django_filters.DateFromToRangeFilter(field_name='argitaratze_data',
    #                                                         widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY/MM'}))
    class Meta:
        model = Jokoa
        fields= ['izena']
