from django import template
from tutoreus.tutorialak.models import Tutoriala
from tutoreus.berriak.models import Berria

register = template.Library()

@register.inclusion_tag('top_tutorialak.html')
def top_tutorialak():
    h = {}
    h['zerr_tutoriala'] = Tutoriala.objects.filter(publikoa_da=True).order_by('-pub_date')[:10]
    return h
 
@register.inclusion_tag('behe_blokeak.html') 
def azken_berriak():
    h = {}
    h['berriak'] = Berria.objects.all().order_by('-pub_date')[:5]
    return h

@register.filter
def mainmenu(url):
    """ """
    mainmenulist = (('','Sarrera'),('nor-gara','Nor gara'),('tutorialak','Tutorialak'),('aplikazioak','Aplikazioak'),('gaiak','Gaiak'),('berriak','Berriak'),('kontaktua','Kontaktua'))
    mainmenu = []
    links = url.strip('/').split('/')
    selected_mainmenu=''
    if len(links)>0 and not links[0]=='':
        selected_mainmenu=links[0]   
    for link,title in mainmenulist:
        if selected_mainmenu==link and len(links)>1:
            mainmenu.append('<li id="active"><a href="/%s" title="%s atal nagusia">%s</a></li>' % (link,title,title))       
        elif selected_mainmenu==link:
            mainmenu.append('<li id="active">%s</li>' % (title))
        else:
            mainmenu.append('<li><a href="/%s" title="%s atal nagusia">%s</a></li>' % (link,title,title))
    return mark_safe(''.join(mainmenu))

