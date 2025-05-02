from .models import Pokemon, PokemonGeneration
from django.contrib import admin


class PokemonGenerationAdmin(admin.ModelAdmin):
    model = PokemonGeneration
    ordering = ["id"]
    list_display = [
        "id",
    ]


class PokemonAdmin(admin.ModelAdmin):
    model = Pokemon
    ordering = ["id"]
    list_filter = ["pokemon_generation"]
    list_display = [
        "id",
        "izena_ingelesez",
        "izena_euskaraz",
        "izena_euskaraz_azalpena",
        "pokemon_generation",
    ]


admin.site.register(PokemonGeneration, PokemonGenerationAdmin)
admin.site.register(Pokemon, PokemonAdmin)
