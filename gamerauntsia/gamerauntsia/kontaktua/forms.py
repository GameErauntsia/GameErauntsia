from django import forms
from django.conf import settings

class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField(widget=TextArea())


    class Meta:
        model = Berria
        fields = '__all__'