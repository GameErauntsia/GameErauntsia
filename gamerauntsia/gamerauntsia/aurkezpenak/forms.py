from django import forms
from django.conf import settings
from gamerauntsia.aurkezpenak.models import Aurkezpena
from tinymce.widgets import TinyMCE

TINYMCE_BODY_CONFIG = getattr(settings, 'TINYMCE_BODY_CONFIG', {})

class AurkezpenaAdminForm(forms.ModelForm):
    slides = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 50,},mce_attrs=TINYMCE_BODY_CONFIG))

    class Meta:
        model = Aurkezpena
        fields = '__all__'
