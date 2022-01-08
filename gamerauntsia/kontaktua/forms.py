from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,
                                  widget=forms.EmailInput(attrs={'placeholder': "nire@helbidea.eus",
                                                                 'class': "form-control"}))
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'placeholder': "Zeri buruz ari zara?",
                                                            'class': "form-control"}))
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={'class': "form-control",
                                                           'cols': "50",
                                                           'rows':"15"}))
    captcha = ReCaptchaField()
