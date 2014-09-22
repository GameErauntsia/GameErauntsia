from django import template
from gamerauntsia.gamer.forms import MyRegistrationForm

register = template.Library()

def regform(request):
    forma=MyRegistrationForm()
    return forma.as_p()

register.simple_tag(regform)
    
