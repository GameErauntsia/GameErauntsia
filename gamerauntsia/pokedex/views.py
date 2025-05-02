from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gamerauntsia.pokedex.models import Pokemon, PokemonGeneration
from gamerauntsia.pokedex.serializers import (
    PokemonSerializer,
    PokemonGenerationSerializer,
)


def pokedex(request):
    return render(request, "pokedex/main.html", locals())


class ApiGetPokemonGenerationList(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        pokemon_generations = PokemonGeneration.objects.all()
        serializer = PokemonGenerationSerializer(pokemon_generations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApiGetPokemonList(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
