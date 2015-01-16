from django import forms
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

    desk = forms.CharField(label='',widget=TinyMCE(
           attrs={'cols': 80, 'rows': 15,},mce_attrs=settings.TINYMCE_BODY_CONFIG))

    gaia = forms.ModelMultipleChoiceField(label='Gaiak', queryset=Gaia.objects.all(),
        widget=forms.SelectMultiple(attrs={'size':'15'}),help_text='Aukeratu artikuluarekin zer ikusia duen gai bat edo gehiago')

    argazkia  = forms.ImageField(label='Nabarmendutako irudia', help_text='Onartutako formatuak: jpg, png, gif.',required=False)

    def clean_desk(self):
        """ """
        desk = self.cleaned_data['desk'].strip()
        if not desk:
            raise forms.ValidationError('Mezu hutsek ez dute balio. Mesedez, idatzi zerbait!')
        return self.cleaned_data['desk']

    def clean_argazkia(self):
        """ """
        argazkia = self.cleaned_data['argazkia']
        if not argazkia:
            return None

        name = argazkia.name
        try:
            name.encode('ascii')
        except:
            raise forms.ValidationError(u'Argazkiaren izenak (%s) karaktere arraroren bat du eta errorea ematen du. Aldatu argazkiari izena, mesedez!' % name)

        if len(name)>90:
            raise forms.ValidationError(u'Argazkiaren izena (%s) luzeegia da. Aldatu argazkiari izena, mesedez!' % name)


        format = name.split('.')[-1]
        if format.lower().strip() not in (u'jpg',u'png',u'gif'):
            raise forms.ValidationError(u'Argazkiaren formatua ez da egokia. Aldatu formatua, mesedez!')

        return argazkia



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

class LastloginForm(forms.ModelForm):

    class Meta:
        model = GamerUser
        fields = ('last_login',)
