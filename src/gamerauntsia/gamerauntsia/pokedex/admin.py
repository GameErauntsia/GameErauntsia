from .models import Pokemon
from django.contrib import admin


class PokemonAdmin(admin.ModelAdmin):
    model = Pokemon
    ordering = ["id"]
    list_display = [
        "id",
        "izena_ingelesez",
        "izena_euskaraz",
        "izena_euskaraz_azalpena",
    ]


admin.site.register(Pokemon, PokemonAdmin)
