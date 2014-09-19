from django import template
from datetime import datetime
from django.db.models import Q
from operator import itemgetter
from datetime import timedelta, date
from django.contrib.contenttypes.models import ContentType

from sustatudjango.base.models import Content
from sustatudjango.content.models import Article, Mezua
from sustatudjango.umapfrontend.models import UmapUrl
from sustatudjango.comments.models import Comment
from sustatudjango.customBlock.models import CustomBlock
from sustatudjango.base.models import Content, Subject
from registration.forms import RegistrationFormUniqueEmail
from sustatudjango.utils.date import convert_tz

register = template.Library()

def regform(request):
    forma=RegistrationFormUniqueEmail()
    #forma.fields['username'].help_text='periko'
    return forma.as_p()

register.simple_tag(regform)

@register.filter
def date_format(date):
    format = ''
    date = convert_tz(date)
    today = convert_tz(datetime.today())
    yesterday = convert_tz(today + timedelta(days=-1))
    if date.strftime("%Y-%m-%d") == today.strftime("%Y-%m-%d"):
        format = 'gaur'
    if date.strftime("%Y-%m-%d") == yesterday.strftime("%Y-%m-%d"):
        format = 'atzo'
    if format not in ('gaur','atzo'):
        format = date.strftime("%Y-%m-%d") + ' : ' + date.strftime("%H:%M")
    else:
        format += date.strftime(" : %H:%M")
    return format
    
