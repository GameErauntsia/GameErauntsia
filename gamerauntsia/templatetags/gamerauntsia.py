from django import template
from registration.forms import RegistrationForm
from django import forms
from django.utils.translation import ugettext_lazy as _

register = template.Library()

def regform(request):
    forma=RegistrationForm()
    return forma.as_p()

register.simple_tag(regform)
    
