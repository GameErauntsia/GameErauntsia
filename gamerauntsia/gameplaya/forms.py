from django import forms
from django.conf import settings
from gamerauntsia.gameplaya.models import GamePlaya
from tinymce.widgets import TinyMCE

TINYMCE_DEFAULT_CONFIG = getattr(settings, "TINYMCE_DEFAULT_CONFIG", {})


class GamePlayAdminForm(forms.ModelForm):
    desk = forms.CharField(
        widget=TinyMCE(
            attrs={
                "cols": 80,
                "rows": 50,
            },
            mce_attrs=TINYMCE_DEFAULT_CONFIG,
        )
    )
    shared = forms.BooleanField(
        label="Sare sozialetan elkarbanatuta",
        help_text="Lauki hau automatikoki markatuko da sistemak edukia sare sozialetan elkarbanatzean.",
        widget=forms.CheckboxInput(attrs={"readonly": "readonly"}),
        required=False,
    )

    class Meta:
        model = GamePlaya
        fields = "__all__"
