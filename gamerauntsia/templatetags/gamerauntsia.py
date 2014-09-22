from django import template

register = template.Library()

from django import forms
from django.utils.translation import ugettext_lazy as _


class GamerRegistration(forms.form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))

def regform(request):
    forma=GamerRegistration()
    return forma.as_p()

register.simple_tag(regform)
    
