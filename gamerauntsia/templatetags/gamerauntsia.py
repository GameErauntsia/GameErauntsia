from django import template
from gamerauntsia.registration.forms import GamerRegistration

register = template.Library()

def regform(request):
    forma=GamerRegistration()
    return forma.as_p()

register.simple_tag(regform)
    
