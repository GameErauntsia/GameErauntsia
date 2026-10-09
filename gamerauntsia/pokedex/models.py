from django.db import models
from django.conf import settings


class PokemonGeneration(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "%d.belaunaldia" % (self.id)

    class Meta:
        verbose_name = "Belaunaldia"
        verbose_name_plural = "Belaunaldiak"


class PokemonResource(models.Model):
    id = models.IntegerField(primary_key=True)
    izena_ingelesez = models.CharField(max_length=256, verbose_name="Izena ingelesez")
    izena_euskaraz = models.CharField(max_length=256, verbose_name="Izena euskaraz")
    deskribapena = models.TextField(max_length=256, null=True, blank=True)


class PokemonItem(PokemonResource):
    def __str__(self):
        return "%d.objektua" % (self.id)

    class Meta:
        verbose_name = "Objektu"
        verbose_name_plural = "Objektuak"


class PokemonCharacter(PokemonResource):
    def __str__(self):
        return "%d.pertsonaia" % (self.id)

    class Meta:
        verbose_name = "Pertsonaia"
        verbose_name_plural = "Pertsonaiak"


class PokemonPokedex(PokemonResource):
    def __str__(self):
        return "%d.pokedexa" % (self.id)

    class Meta:
        verbose_name = "Pokedexa"
        verbose_name_plural = "Pokedexak"


class PokemonType(PokemonResource):
    def __str__(self):
        return "%d.mota" % (self.id)

    class Meta:
        verbose_name = "Mota"
        verbose_name_plural = "Motak"


class PokemonAbility(PokemonResource):
    def __str__(self):
        return "%d.gaitasuna" % (self.id)

    class Meta:
        verbose_name = "Gaitasuna"
        verbose_name_plural = "Gaitasunak"


class PokemonMove(PokemonResource):
    def __str__(self):
        return "%d.erasoa" % (self.id)

    class Meta:
        verbose_name = "Erasoa"
        verbose_name_plural = "Erasoak"


class PokemonRegion(PokemonResource):
    def __str__(self):
        return "%d.lurraldea" % (self.id)

    class Meta:
        verbose_name = "Lurraldea"
        verbose_name_plural = "Lurradeak"


class PokemonLocation(PokemonResource):
    def __str__(self):
        return "%d.tokia" % (self.id)

    class Meta:
        verbose_name = "Tokia"
        verbose_name_plural = "Tokiak"


class PokemonNature(PokemonResource):
    def __str__(self):
        return "%d.izaera" % (self.id)

    class Meta:
        verbose_name = "Izaera"
        verbose_name_plural = "Izaerak"


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    pokemon_generation = models.ForeignKey(
        PokemonGeneration,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="Belaunaldia",
    )
    izena_ingelesez = models.CharField(max_length=256, verbose_name="Izena ingelesez")
    izena_euskaraz = models.CharField(max_length=256, verbose_name="Izena euskaraz")
    izena_euskaraz_azalpena = models.CharField(
        max_length=256, verbose_name="Euskarazko izenaren azalpen laburra"
    )
    deskribapena = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "Pokemon - %d" % (self.id)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemonak"
