from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^api/pokemon", ApiGetPokemonList.as_view(), name="api_pokemon_list"),
    url(r"", pokedex, name="pokedex"),
]
