from django import forms
from django.conf import settings
from models import Finished


class FinishedForm(forms.ModelForm):
    jokoa = forms.CharField(label="Jokoa", widget=forms.Textarea)
    nota = forms.DecimalField(label="Nota")
    fetxa = forms.DateTimeField(
        label=_("Fetxa"), widget=DateTimeWidget(usel10n=True, bootstrap_version=3)
    )

    class Meta:
        model = Finished
