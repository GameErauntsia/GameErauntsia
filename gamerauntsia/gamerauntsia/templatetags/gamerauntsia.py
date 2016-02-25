from django import template
from registration.forms import RegistrationFormUniqueEmail
from photologue.models import Photo
from bootstrapform.templatetags.bootstrap import bootstrap
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
    forma = RegistrationFormUniqueEmail()
    return bootstrap(forma)

register.simple_tag(regform)

def steam_panel():
    try:
        steam_group = dict(dict(get_urlxml('http://steamcommunity.com/groups/gamerauntsia/memberslistxml/')['memberList'])['groupDetails'])
        return {'steam_group': steam_group}
    except:
        return {'steam_group': None}
register.inclusion_tag('steam_panel.html')(steam_panel)

@register.filter
def check_seen(obj,user):
    return obj.has_seen(user)

@register.filter
def get_photo_url(obj_id):
    return Photo.objects.get(id=obj_id).get_newsprofile_url()
