from django import forms
from gamerauntsia.gamer.models import GamerUser

class PersonalForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('fullname','bio')