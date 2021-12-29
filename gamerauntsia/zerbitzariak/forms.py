from django import forms
from .models import MC_Whitelist
from gamerauntsia.gamer.models import MC_PLATFORMS

class MCForm(forms.ModelForm):
    mc_user = forms.CharField(label="Minecraft erabiltzailea")
    platform = forms.ChoiceField(choices=MC_PLATFORMS, label="Minecraft edizioa")
    lizentzia = forms.BooleanField(label="Onartzen ditut Minecraft zerbitzariko araudi eta baldintzak.", required=True)

    class Meta:
        model = MC_Whitelist
        fields = ('platform','mc_user', 'lizentzia')
