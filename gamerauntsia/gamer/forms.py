from django import forms
from gamerauntsia.gamer.models import GamerUser, JokuPlataforma
from django.utils.translation import ugettext as _

class NotifyForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('email_notification',)

class GameForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput())

    class Meta:
        model = JokuPlataforma
        fields = ('plataforma','nick')