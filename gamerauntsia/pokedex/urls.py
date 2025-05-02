from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r"^api/pokemons", ApiGetPokemonList.as_view(), name="api_pokemon_list"),
    re_path(
        r"^api/pokemon-generations",
        ApiGetPokemonGenerationList.as_view(),
        name="api_pokemon_generation_list",
    ),
    re_path(r"", pokedex, name="pokedex"),
]
