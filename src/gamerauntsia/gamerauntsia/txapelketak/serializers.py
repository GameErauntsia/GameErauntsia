from rest_framework import serializers
from gamerauntsia.txapelketak.models import Txapelketa


class TxapelketaSerializer(serializers.ModelSerializer):
    irudia = serializers.ReadOnlyField(source="irudia.get_blog_url")
    irudia2 = serializers.ReadOnlyField(source="irudia.image.url")

    class Meta:
        model = Txapelketa
        depth = 2
        fields = (
            "id",
            "izena",
            "desk",
            "arauak",
            "saria",
            "irudia",
            "irudia2",
            "mota",
            "modalitatea",
            "status",
            "pub_date",
            "insk_date",
            "jokalariak",
        )
