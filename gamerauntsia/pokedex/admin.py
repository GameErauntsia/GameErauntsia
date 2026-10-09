from .models import (
    Pokemon,
    PokemonGeneration,
    PokemonItem,
    PokemonCharacter,
    PokemonPokedex,
    PokemonType,
    PokemonAbility,
    PokemonMove,
    PokemonRegion,
    PokemonLocation,
    PokemonNature,
)
from django.contrib import admin


class PokemonGenerationAdmin(admin.ModelAdmin):
    model = PokemonGeneration
    ordering = ["id"]
    list_display = [
        "id",
    ]


class PokemonResourceAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "izena_ingelesez", "izena_euskaraz"]


class PokemonItemAdmin(PokemonResourceAdmin):
    model = PokemonItem


class PokemonCharacterAdmin(PokemonResourceAdmin):
    model = PokemonCharacter


class PokemonTypeAdmin(PokemonResourceAdmin):
    model = PokemonType


class PokemonPokedexAdmin(PokemonResourceAdmin):
    model = PokemonPokedex


class PokemonAbilityAdmin(PokemonResourceAdmin):
    model = PokemonAbility


class PokemonMoveAdmin(PokemonResourceAdmin):
    model = PokemonMove


class PokemonRegionAdmin(PokemonResourceAdmin):
    model = PokemonRegion


class PokemonLocationAdmin(PokemonResourceAdmin):
    model = PokemonLocation


class PokemonNatureAdmin(PokemonResourceAdmin):
    model = PokemonNature


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
admin.site.register(PokemonItem, PokemonItemAdmin)
admin.site.register(PokemonCharacter, PokemonCharacterAdmin)
admin.site.register(PokemonType, PokemonTypeAdmin)
admin.site.register(PokemonPokedex, PokemonPokedexAdmin)
admin.site.register(PokemonAbility, PokemonAbilityAdmin)
admin.site.register(PokemonMove, PokemonMoveAdmin)
admin.site.register(PokemonRegion, PokemonRegionAdmin)
admin.site.register(PokemonLocation, PokemonLocationAdmin)
admin.site.register(PokemonNature, PokemonNatureAdmin)
admin.site.register(Pokemon, PokemonAdmin)
