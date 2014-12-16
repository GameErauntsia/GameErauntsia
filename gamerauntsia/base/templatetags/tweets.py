from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def renderText(tweet):
    """ """
    if tweet.retweeted:
        text = tweet.retweeted.text
    else:
        text = tweet.text
        
    ws = []
    for w in text.split():
        if w.startswith('http://') or w.startswith('https://'):
            ws.append(u'<a target="_top" href="%s" target="_blank" rel="nofollow">%s</a>' % (w,w))
        elif w.startswith('#'):
            ws.append(u'<a target="_top" href="http://twitter.com/#!/search?q=%%23%s" >%s</a>' % (w[1:],w))            
        elif w.startswith('@'):
            ws.append(u'<a target="_top" href="http://twitter.com/#!/%s" >%s</a>' % (w[1:],w))            
        else:
            ws.append(w)
    return u' '.join(ws)