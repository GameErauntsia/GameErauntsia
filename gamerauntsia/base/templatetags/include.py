from django import template
from django.utils.safestring import mark_safe
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria
from gamerauntsia.gamer.models import GamerUser
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django_messages.models import Message

register = template.Library()

@register.inclusion_tag('top_gameplayak.html')
def top_gameplayak():
    h = {}
    h['zerr_tutoriala'] = GamePlaya.objects.filter(publikoa_da=True).order_by('-pub_date')[:10]
    return h
 
@register.inclusion_tag('behe_blokeak.html') 
def azken_berriak():
    h = {}
    h['berriak'] = Berria.objects.all().order_by('-pub_date')[:5]
    return h

@register.filter
def mainmenu(url):
    """ """
    mainmenulist = (('','Sarrera'),('gameplayak','GamePlayak'),('jokoak','Jokoak'),('gaiak','Gaiak'),('berriak','Berriak'),('nor-gara','Nor gara'),('kontaktua','Kontaktua'))
    mainmenu = []
    links = url.strip('/').split('/')
    selected_mainmenu=''
    if len(links)>0 and not links[0]=='':
        selected_mainmenu=links[0]
    for link,title in mainmenulist:
        if selected_mainmenu==link and len(links)>1:
            mainmenu.append('<li class="active"><a href="/%s" title="%s">%s</a></li>' % (link,title,title))      
        elif selected_mainmenu==link:
            mainmenu.append('<li class="active">%s</li>' % (title))
        else:
            if link=='' and selected_mainmenu=='sarrera':
                mainmenu.append('<li class="active"><a href="/" title="%s">%s</a></li>' % (title,title))
            else:
                mainmenu.append('<li><a href="/%s" title="%s">%s</a></li>' % (link,title,title))
    return mark_safe(''.join(mainmenu))

@register.filter
def tabmenu(url):
    """ """
    mainmenulist = (('','Azkenak'),('bozkatuenak','Bozkatuenak'))
    mainmenu = []
    links = url.strip('/').split('/')
    selected_mainmenu=''
    if len(links)>0 and not links[0]=='':
        selected_mainmenu=links[1]
    for link,title in mainmenulist:
        if selected_mainmenu==link:
            mainmenu.append('<li class="selected">%s</li>' % (title))     
        else:
            if selected_mainmenu=='':
                mainmenu.append('<li><a href="/sarrera/%s" title="%s">%s</a></li>' % (link,title,title))
            else:
                mainmenu.append('<li><a href="/%s" title="%s">%s</a></li>' % (link,title,title))
    return mark_safe(''.join(mainmenu))

@register.filter
def get_bideo(item):
    html = ''
    if item.bideoa.startswith('http://vimeo.com'):
        html = '<iframe class="shadow" src="http://player.vimeo.com/video/'+item.get_url()+'" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>'
    elif item.bideoa.startswith('http://youtu.be'):
        html = '<iframe class="shadow" width="500" height="281" src="http://www.youtube.com/embed/'+item.get_url()+'" frameborder="0" allowfullscreen></iframe>'
    else:
        html = ''
    return html


@register.filter
def contains(value, arg):
  """
  Usage:
  {% if text|contains:"http://" %}
  This is a link.
  {% else %}
  Not a link.
  {% endif %}
  """
  if arg in value:
    return True
  return False

@register.filter
def isequal(value, arg):
  if arg == value:
    return True
  return False

@register.filter
def urlfriend(value):
    return value.replace(' ', '%20')

@register.inclusion_tag('comments/last.html')
def azken_erantzunak(model='Berria'):
    h = {}
    ct = ContentType.objects.get(model=model)
    h['comments'] = Comment.objects.filter(content_type=ct).order_by('-submit_date')[:5]
    return h

@register.filter
def ken1(value):
    return value-1

@register.filter
def irekita(value):
    if value > timezone.now():
        return True
    return False

@register.filter
def inbox_count_for(user):
    return Message.objects.filter(recipient=user, read_at__isnull=True, recipient_deleted_at__isnull=True).count()
