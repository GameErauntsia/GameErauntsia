from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tutorialak.models import Tutoriala
from base.models import Base
from berriak.models import Berria

def index(request):
    h = {}
    tutorial_list = Tutoriala.objects.all().order_by('-pub_date')
    paginator = Paginator(tutorial_list, 8)
    page = request.GET.get('orria')
    try:
        tutorialak = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tutorialak = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tutorialak = paginator.page(paginator.num_pages)
    h['base'] = Base.objects.all()[0]
    h['tutorialak'] = tutorialak
    return render_to_response('base/index.html', h,context_instance=RequestContext(request))