from django import forms
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class FlatPageForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs=settings.TINYMCE_DEFAULT_CONFIG))

    class Meta:
        model = FlatPage
        fields = "__all__"