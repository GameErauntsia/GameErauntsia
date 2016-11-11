from gamerauntsia.bazkidetza.models import Eskaintza, Bazkidea
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.shortcuts import render
from django.db.models import Q

def index(request):
    if request.user.is_authenticated():
        bazkidea = request.user.get_bazkidea()
    eskaintzak = Eskaintza.objects.filter(Q(is_public=True), Q(expire_date__gte=datetime.now()) | Q(expire_date__isnull=True)).order_by('-activate_date')
    return render(request, 'bazkidetza/index.html', locals())

def eskaintza(request, slug):
    if request.user.is_authenticated():
        bazkidea = request.user.get_bazkidea()
    eskaintza = get_object_or_404(Eskaintza, slug=slug, is_public=True)
    return render(request, 'bazkidetza/eskaintza.html', locals())

def create_bazkidea(request):
    if not Bazkidea.objects.filter(user=request.user).exists():
    	bazkide = Bazkidea(user=request.user, is_active=True)
    	bazkide.save()
    return HttpResponseRedirect(reverse('bazkidetza'))

def payment_done(request):
    if request.user.is_authenticated() and Bazkidea.objects.filter(user=request.user).exists():
        bazkide = Bazkidea.objects.get(user=request.user)
        bazkide.paid = True
        bazkide.save()
    return HttpResponseRedirect(reverse('bazkidetza'))