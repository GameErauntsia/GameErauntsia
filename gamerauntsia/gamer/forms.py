from django import forms
from gamerauntsia.berriak.models import Berria, Gaia
from gamerauntsia.gamer.models import GamerUser, JokuPlataforma
from gamerauntsia.gameplaya.models import Kategoria, GamePlaya
from gamerauntsia.jokoa.models import Jokoa
from tinymce.widgets import TinyMCE
from django.conf import settings

class GamerForm(forms.ModelForm):

    signature = forms.CharField(widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_SMALL_BODY_CONFIG),required=False)

    class Meta:
        model = GamerUser
        fields = ('fullname','bio','twitter_id','facebook_id','ytube_channel','signature')

class PCForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('motherboard','processor','graphics','soundcard','ram','harddrive','harddrive2','mouse','keyboard','speakers')


class NotifyForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('email_notification','buletin_notification')

class ArticleForm(forms.ModelForm):

    desk = forms.CharField(label='',widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    gaia = forms.ModelMultipleChoiceField(label='Gaiak', queryset=Gaia.objects.all(),
        widget=forms.SelectMultiple(attrs={'size':'15'}),help_text='Aukeratu artikuluarekin zer ikusia duen gai bat edo gehiago')

    argazkia  = forms.ImageField(label='Nabarmendutako irudia', help_text='Onartutako formatuak: jpg, png, gif.', required=False)

    def clean_desk(self):
        """ """
        desk = self.cleaned_data['desk'].strip()
        if not desk:
            raise forms.ValidationError('Mezu hutsek ez dute balio. Mesedez, idatzi zerbait!')
        return self.cleaned_data['desk']

    class Meta:
        model = Berria
        exclude = ('slug','erabiltzailea','pub_date','publikoa_da','status','mod_date','shared')

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


class GamePlayForm(forms.ModelForm):

    desk = forms.CharField(label='',widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_SMALL_BODY_CONFIG))

    kategoria = forms.ModelMultipleChoiceField(label='Gaiak', queryset=Kategoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'size':'15'}),help_text='Aukeratu artikuluarekin zer ikusia duen gai bat edo gehiago')

    argazkia  = forms.ImageField(label='Nabarmendutako irudia', help_text='Onartutako formatuak: jpg, png, gif.', required=False)

    jokoa = forms.ModelChoiceField(label="Jokoa", queryset=Jokoa.objects.all().order_by('izena'))

    def clean_desk(self):
        """ """
        desk = self.cleaned_data['desk'].strip()
        if not desk:
            raise forms.ValidationError('Mezu hutsek ez dute balio. Mesedez, idatzi zerbait!')
        return self.cleaned_data['desk']

    class Meta:
        model = GamePlaya
        exclude = ('slug','erabiltzailea','pub_date','publikoa_da','status','mod_date','shared','argazkia')
