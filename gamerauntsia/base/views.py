from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gamerauntsia.gameplaya.models import GamePlaya
from gamerauntsia.berriak.models import Berria

def index(request):
    h = {}
    tutorial_list = GamePlaya.objects.filter(publikoa_da=True).order_by('-pub_date')
    paginator = Paginator(tutorial_list, 8)
    page = request.GET.get('orria')
    try:
        gameplayak = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gameplayak = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gameplayak = paginator.page(paginator.num_pages)
    except:
        raise Http404 
    h['gameplayak'] = gameplayak
    return render_to_response('base.html', h,context_instance=RequestContext(request))

def google(request):
    h = {}
    return render_to_response('googleaf6b2cbbb22dca3f.html', h,context_instance=RequestContext(request))

def rating(request):
    value = request.GET.get('value')
    slug = request.GET.get('slug')
    tutoriala = get_object_or_404(GamePlaya,slug=slug)
    if tutoriala:
        tutoriala.botoak += 1
        tutoriala.puntuak += float(value)/2
        tutoriala.save()
    	return HttpResponse('True')
    return HttpResponse('False')
