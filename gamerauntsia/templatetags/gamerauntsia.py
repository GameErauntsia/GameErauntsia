from django import template
from registration.forms import RegistrationForm
from django import forms
import urllib2
import xmltodict
from django.utils.translation import ugettext_lazy as _

register = template.Library()

def get_urlxml(url):
    stream = []
    raw_data = urllib2.urlopen(url)
    data = raw_data.read()
    raw_data.close()
    stream = dict(xmltodict.parse(data))
    return stream

def regform(request):
    forma=RegistrationForm()
    return forma.as_p()

register.simple_tag(regform)

def steam_panel():
    steam_group = dict(dict(get_urlxml('http://steamcommunity.com/groups/gamerauntsia/memberslistxml/')['memberList'])['groupDetails'])
    return {'steam_group': steam_group}
register.inclusion_tag('steam_panel.html')(steam_panel)