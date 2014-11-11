from django import forms
from gamerauntsia.gamer.models import GamerUser, JokuPlataforma
from django.utils.translation import ugettext as _

class GamerForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('fullname','bio','signature')

class NotifyForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('email_notification',)

class GameForm(forms.ModelForm):

    class Meta:
        model = JokuPlataforma
        fields = ('plataforma','nick')