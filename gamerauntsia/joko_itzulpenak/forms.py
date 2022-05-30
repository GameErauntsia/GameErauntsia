from django import forms
from django.conf import settings
from gamerauntsia.joko_itzulpenak.models import ItzulpenProiektua
from tinymce.widgets import TinyMCE

TINYMCE_DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', {})

class ItzulpenProiektuaAdminForm(forms.ModelForm):
    deskribapena = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 10,},mce_attrs=TINYMCE_DEFAULT_CONFIG))
    instalazioa = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30,},mce_attrs=TINYMCE_DEFAULT_CONFIG))
    ohar_teknikoak = forms.CharField(widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30,},mce_attrs=TINYMCE_DEFAULT_CONFIG), required=False)

    class Meta:
        model = ItzulpenProiektua
        fields = '__all__'
