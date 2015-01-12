from django import forms
from django.conf import settings
from gamerauntsia.berriak.models import Berria
from tinymce.widgets import TinyMCE

class BerriaAdminForm(forms.ModelForm):
    desk = forms.CharField(widget=TinyMCE(
               attrs={'cols': 80, 'rows': 50,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    class Meta:
        model = Berria
