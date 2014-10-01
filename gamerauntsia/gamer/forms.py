from django import forms
from hiribili.hiribiliuser.models import GamerUser
from django.utils.translation import ugettext as _

class NotifyForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('email_notification',)