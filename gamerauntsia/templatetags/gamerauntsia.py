from django import template
from gamerauntsia.gamer.forms import MyRegistrationFormUniqueEmail

register = template.Library()

def regform(request):
    forma=MyRegistrationFormUniqueEmail()
    return forma.as_p()

register.simple_tag(regform)
    
