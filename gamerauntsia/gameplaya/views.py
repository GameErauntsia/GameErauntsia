from gamerauntsia.gameplaya.models import GamePlaya, Gaia, Zailtasuna
from gamerauntsia.jokoa.models import Jokoa
from gamerauntsia.berriak.models import Berria
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404

def index(request,gaia=None,username=None):
    if gaia:
        gaia = get_object_or_404(Gaia,slug=gaia)
        gameplayak = GamePlaya.objects.filter(publikoa_da=True,gaia=gaia).order_by('-pub_date')
    elif username:
        user = get_object_or_404(User,user=username)
        gameplayak = GamePlaya.objects.filter(publikoa_da=True,user=user).order_by('-pub_date')
    else:
        gameplayak = GamePlaya.objects.filter(publikoa_da=True).order_by('-pub_date')
    users = User.objects.all()
    gaiak = Gaia.objects.all()
    zailtasunak = Zailtasuna.objects.all()
    return render_to_response('gameplaya/index.html', locals(),context_instance=RequestContext(request))
    
def gameplaya(request,slug):
    gp = get_object_or_404(GamePlaya,slug=slug)
    return render_to_response('gameplaya/gameplay.html', locals(),context_instance=RequestContext(request))
    
def gaiak(request):
    h = {}
    h['gaiak'] = Gaia.objects.all()
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('gameplaya/gaiak.html', h,context_instance=RequestContext(request))
    
def gaia(request,slug):
    h = {}
    h['zerr_tutoriala'] = GamePlaya.objects.filter(gaia__slug=slug, publikoa_da=True).order_by('-pub_date')[:10]
    h['gaia'] = Gaia.objects.filter(slug=slug)[0]
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('gameplaya/gaia.html', h,context_instance=RequestContext(request))
    
def gameplaya_aplikazioa(request,aplikazioa):
    h = {}
    tutorial_list = GamePlaya.objects.filter(aplikazioa__izena=aplikazioa,publikoa_da=True).order_by('-pub_date')
    paginator = Paginator(tutorial_list, 6)
    page = request.GET.get('orria')
    try:
        gameplaya = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gameplaya = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gameplaya = paginator.page(paginator.num_pages)
    h['gameplaya'] = gameplaya
    h['aplikazioa'] = Jokoa.objects.get(izena=aplikazioa)
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('gameplaya/gameplaya_aplikazioa.html', h,context_instance=RequestContext(request))
    
def gameplaya_gaia(request,gaia):
    h = {}
    tutorial_list = GamePlaya.objects.filter(gaia__izena=gaia,publikoa_da=True).order_by('-pub_date')
    paginator = Paginator(tutorial_list, 6)
    page = request.GET.get('orria')
    try:
        gameplaya = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gameplaya = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gameplaya = paginator.page(paginator.num_pages)
    h['gameplaya'] = gameplaya
    h['gaia'] = Gaia.objects.get(izena=gaia)
    h['zerr_tutoriala'] = GamePlaya.objects.filter(publikoa_da=True).order_by('-pub_date')[:10]
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('gameplaya/gameplaya_gaia.html', h,context_instance=RequestContext(request))   
    
    
def bozkatuenak(request):
    h = {}
    tutorial_list = GamePlaya.objects.filter(publikoa_da=True).order_by('-puntuak','-botoak')
    paginator = Paginator(tutorial_list, 8) # Show 25 contacts per page
    page = request.GET.get('orria')
    try:
        gameplaya = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gameplaya = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gameplaya = paginator.page(paginator.num_pages)
    except:
        return Http404
    h['gameplaya'] = gameplaya
    h['berriak'] = Berria.objects.filter(publikoa_da=True).order_by('-pub_date')[:5]
    return render_to_response('base/index.html', h,context_instance=RequestContext(request))
