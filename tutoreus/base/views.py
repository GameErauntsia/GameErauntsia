from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tutoreus.tutorialak.models import Tutoriala
from tutoreus.base.models import Base
from tutoreus.berriak.models import Berria

def index(request):
    h = {}
    tutorial_list = Tutoriala.objects.all().order_by('-pub_date')
    paginator = Paginator(tutorial_list, 8)
    page = request.GET.get('orria')
    try:
        tutorialak = paginator.page(page)
        h['base'] = Base.objects.all()[0]
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tutorialak = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tutorialak = paginator.page(paginator.num_pages)
    except:
        raise Http404 
    h['tutorialak'] = tutorialak
    return render_to_response('base/index.html', h,context_instance=RequestContext(request))

def google(request):
    h = {}
    return render_to_response('googleaf6b2cbbb22dca3f.html', h,context_instance=RequestContext(request))

def rating(request):
    value = request.GET.get('value')
    slug = request.GET.get('slug')
    tutoriala = get_object_or_404(Tutoriala,slug=slug)
    if tutoriala:
        tutoriala.botoak += 1
        tutoriala.puntuak += float(value)/2
        tutoriala.save()
    	return HttpResponse('True')
    return HttpResponse('False')
