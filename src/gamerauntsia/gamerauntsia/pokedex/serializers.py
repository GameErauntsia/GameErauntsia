from rest_framework.serializers import ModelSerializer
from gamerauntsia.pokedex.models import Pokemon


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            "id",
            "izena_ingelesez",
            "izena_euskaraz",
            "izena_euskaraz_azalpena",
            "deskribapena",
        ]
