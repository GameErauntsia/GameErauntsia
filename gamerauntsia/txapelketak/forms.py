from django import forms
from models import Partaidea

class PartidaInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartidaInlineForm, self).__init__(*args, **kwargs)
        if self.instance:
        	self.fields['partaideak'].queryset = Partaidea.objects.filter(
            txapelketa=self.instance)