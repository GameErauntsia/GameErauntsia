from django import forms
from gamerauntsia.gamer.models import GamerUser, JokuPlataforma
from gamerauntsia.jokoa.models import Jokoa
from tinymce.widgets import TinyMCE
from django.conf import settings
from django.utils.translation import ugettext as _

class GamerForm(forms.ModelForm):

    signature = forms.CharField(widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    class Meta:
        model = GamerUser
        fields = ('fullname','bio','signature')

class NotifyForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('email_notification',)

class TopForm(forms.ModelForm):

    top_jokoak = forms.ModelMultipleChoiceField(Jokoa.objects.all(), widget=FilteredSelectMultiple("Jokoa", False, attrs={'rows':'2'}))

    class Meta:
        model = GamerUser
        fields = ('top_jokoak',)

class GameForm(forms.ModelForm):

    class Meta:
        model = JokuPlataforma
        fields = ('plataforma','nick')