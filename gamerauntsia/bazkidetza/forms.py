from django import forms
from django.conf import settings
from gamerauntsia.bazkidetza.models import Eskaintza
from tinymce.widgets import TinyMCE

TINYMCE_DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})

class EskaintzaAdminForm(forms.ModelForm):
    deskribapena = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 50,},mce_attrs=TINYMCE_DEFAULT_CONFIG))
    
    class Meta:
        model = Eskaintza
        fields = '__all__'