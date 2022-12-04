from django import forms
from django.conf import settings
from gamerauntsia.jokoen_itzulpenak.models import EuskarazkoJokoa
from tinymce.widgets import TinyMCE

TINYMCE_DEFAULT_CONFIG = getattr(settings, "TINYMCE_DEFAULT_CONFIG", {})


class EuskarazkoJokoaAdminForm(forms.ModelForm):
    instalazioa = forms.CharField(
        widget=TinyMCE(
            attrs={
                "cols": 80,
                "rows": 50,
            },
            mce_attrs=TINYMCE_DEFAULT_CONFIG,
        )
    )

    class Meta:
        model = EuskarazkoJokoa
        fields = "__all__"
