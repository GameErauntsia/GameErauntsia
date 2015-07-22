from django import forms
from django.conf import settings
from gamerauntsia.aurkezpenak.models import Aurkezpena
from tinymce.widgets import TinyMCE

class AurkezpenaAdminForm(forms.ModelForm):
    slides = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 50,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    class Meta:
        model = Aurkezpena
