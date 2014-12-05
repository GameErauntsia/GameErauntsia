from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from models import Partaidea, Txapelketa

class PartidaInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartidaInlineForm, self).__init__(*args, **kwargs)
        if self.instance:
        	self.fields['partaideak'].queryset = Partaidea.objects.filter(
            txapelketa=self.instance)


class TxapelketaAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=settings.TINYMCE_BODY_CONFIG))
    arauak = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    class Meta:
        model = Txapelketa