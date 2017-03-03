from django import template
from photologue.models import Photo
import urllib2
import xmltodict

register = template.Library()


def get_urlxml(url):
    stream = []
    raw_data = urllib2.urlopen(url)
    data = raw_data.read()
    raw_data.close()
    stream = dict(xmltodict.parse(data))
    return stream


def steam_panel():
    try:
        steam_group = dict(dict(get_urlxml('http://steamcommunity.com/groups/gamerauntsia/memberslistxml/')['memberList'])['groupDetails'])
        return {'steam_group': steam_group}
    except:
        return {'steam_group': None}
register.inclusion_tag('steam_panel.html')(steam_panel)


@register.filter
def check_seen(obj, user):
    return obj.has_seen(user)


@register.filter
def get_photo_url(obj_id):
    return Photo.objects.get(id=obj_id).get_newsprofile_url()
