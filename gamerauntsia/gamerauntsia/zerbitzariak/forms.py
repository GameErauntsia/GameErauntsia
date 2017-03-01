from django import forms
from .models import MC_Whitelist

class MCForm(forms.ModelForm):
    mc_user = forms.CharField(label="Minecraft erabiltzailea")
    lizentzia = forms.BooleanField(label="Onartzen ditut Minecraft zerbitzariko araudi eta baldintzak.", required=False)

    class Meta:
        model = MC_Whitelist
        fields = ('mc_user','lizentzia')