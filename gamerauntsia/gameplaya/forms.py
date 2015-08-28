from django import forms
from django.conf import settings
from gamerauntsia.gameplaya.models import GamePlaya
from tinymce.widgets import TinyMCE

class GamePlayAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 50,},mce_attrs=settings.TINYMCE_BODY_CONFIG))
    shared = forms.BooleanField(label="Sare sozialetan elkarbanatuta",widget = forms.CheckboxInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = GamePlaya	
