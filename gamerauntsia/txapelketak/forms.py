from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from models import Partaidea, Txapelketa

TINYMCE_BODY_CONFIG = getattr(settings, 'TINYMCE_BODY_CONFIG', {})

class PartidaInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartidaInlineForm, self).__init__(*args, **kwargs)
        if self.instance:
        	self.fields['partaideak'].queryset = Partaidea.objects.filter(
            txapelketa=self.instance)


class TxapelketaAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=TINYMCE_BODY_CONFIG))
    arauak = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=TINYMCE_BODY_CONFIG))
    saria = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 30,},mce_attrs=TINYMCE_BODY_CONFIG))
               
    shared = forms.BooleanField(label="Sare sozialetan elkarbanatuta",help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.", widget = forms.CheckboxInput(attrs={'readonly':'readonly'}),required=False)

    class Meta:
        model = Txapelketa
