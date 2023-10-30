import django_filters
from gamerauntsia.jokoa.models import (
    Garatzailea,
    Jokoa,
    Plataforma,
    Generoa,
    SOFTWARE_AUKERAK,
)
from gamerauntsia.joko_itzulpenak.models import ITZULPEN_JATORRIAK

BOOLEAN_CHOICES = (
    (True, "Bai"),
    (False, "Ez"),
)


class JokoGaratzaileakFilter(django_filters.FilterSet):
    izena = django_filters.CharFilter(lookup_expr="icontains", label="Bilatu izenez")
    plataformak = django_filters.ModelMultipleChoiceFilter(
        field_name="plataformak", queryset=Plataforma.objects, label="Plataformak"
    )

    class Meta:
        model = Garatzailea
        fields = [
            "izena",
        ]


class EuskarazkoJokoaFilter(django_filters.FilterSet):
    izena = django_filters.CharFilter(lookup_expr="icontains", label="Bilatu izenez")
    plataformak = django_filters.ModelMultipleChoiceFilter(
        field_name="jokoitzulpena__plataformak",
        queryset=Plataforma.objects,
        label="Plataformak",
    )
    generoak = django_filters.ModelMultipleChoiceFilter(
        field_name="generoak", queryset=Generoa.objects, label="Generoak"
    )
    lizentzia = django_filters.ChoiceFilter(
        field_name="lizentzia",
        choices=SOFTWARE_AUKERAK,
        label="Lizentzia",
        empty_label="-",
    )
    ofiziala_da = django_filters.ChoiceFilter(
        field_name="jokoitzulpena__ofiziala_da",
        choices=BOOLEAN_CHOICES,
        label="Ofiziala",
        empty_label="-",
    )
    jatorria = django_filters.ChoiceFilter(
        field_name="jokoitzulpena__jatorria",
        choices=ITZULPEN_JATORRIAK,
        label="Mota",
        empty_label="-",
    )

    ordena = django_filters.OrderingFilter(
        fields=(("izena", "izena"), ("argitaratze_data", "argitaratze_data")),
        choices=(
            ("izena", "Izena (a-z)"),
            ("-izena", "Izena (z-a)"),
            ("-argitaratze_data", "Argitaratze data (berrienak lehenengo)"),
            ("argitaratze_data", "Argitaratze data (zaharrenak lehenengo)"),
            (
                "-jokoitzulpena__erabilgarritasun_data",
                "Euskaratze data (berrienak lehenengo)",
            ),
            (
                "jokoitzulpena__erabilgarritasun_data",
                "Euskaratze data (zaharrenak lehenengo)",
            ),
        ),
        empty_label="-",
    )

    class Meta:
        model = Jokoa
        fields = ["izena"]
