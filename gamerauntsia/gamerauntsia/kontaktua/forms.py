from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    captcha = ReCaptchaField(label="")