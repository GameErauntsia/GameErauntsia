#from gamerauntsia.gamer.models import GamerUser
from django import forms
from django.utils.translation import ugettext_lazy as _


class GamerRegistration(forms.form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = forms.EmailField(label=_("E-mail"))

    # def clean_email(self):
    #     """
    #     Validate that the supplied email address is unique for the
    #     site.
        
    #     """
    #     if GamerUser.objects.filter(email__iexact=self.cleaned_data['email']):
    #         raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
    #     return self.cleaned_data['email']