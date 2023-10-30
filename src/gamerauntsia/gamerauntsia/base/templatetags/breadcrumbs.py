from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def breadcrumbs(url):
    home = [
        '<strong>Hemen zaude</strong>: <a href="/" title="Sarrera orrira lotura">Sarrera</a> &raquo;',
    ]
    links = url.strip("/").split("/")
    bread = []
    total = len(links) - 1
    for i, link in enumerate(links):
        if not link == "":
            bread.append(link)
            this_url = "/".join(bread)
            sub_link = link.replace("-", " ").replace("?", "").replace("=", ", ")
            sub_link = sub_link.title()
            if not i == total:
                tlink = '<a href="/%s/" title="%s orrira lotura">%s</a> &raquo;' % (
                    this_url,
                    sub_link,
                    sub_link,
                )
            else:
                tlink = "%s" % sub_link
            home.append(tlink)
    bcrumb = " ".join(home)
    return mark_safe(bcrumb)


@register.filter
def get_range(value):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
    """
    return range(value)
