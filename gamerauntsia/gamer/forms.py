from django import forms
from django.forms.extras.widgets import SelectDateWidget
from gamerauntsia.berriak.models import Berria, Gaia
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

class ArticleForm(forms.ModelForm):

    desk = forms.CharField(widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_BODY_CONFIG))
    argazkia  = forms.ImageField(label='Nabarmendutako irudia', help_text='Onartutako formatuak: jpg, png, gif.',required=False)

    pub_date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Berria
        exclude = ('slug','erabiltzailea','publikoa_da','status','mod_date','shared')

class TopForm(forms.ModelForm):

    top_jokoak = forms.ModelMultipleChoiceField(queryset=Jokoa.objects.all().order_by('izena','bertsioa'),
                                          label='',
                                          required=False,
                                          widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = GamerUser
        fields = ('top_jokoak',)

class GameForm(forms.ModelForm):

    class Meta:
        model = JokuPlataforma
        fields = ('plataforma','nick')

class LastloginForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('last_login',)
