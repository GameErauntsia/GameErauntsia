from django.shortcuts import render
from django.shortcuts import get_object_or_404
from gamerauntsia.joko_itzulpenak.models import ItzulpenProiektua
from gamerauntsia.jokoa.models import Jokoa

def itzulpen_proiektua(request,slug):
    proiektua = get_object_or_404(ItzulpenProiektua,slug=slug)
    parte_hartzaileak = proiektua.itzulpenproiektupartehartzailea_set.all()
    return render(request, 'joko_itzulpenak/proiektua.html',locals())

def itzulpen_proiektuak(request):
    proiektuak = ItzulpenProiektua.objects.prefetch_related('jokoa','jokoa__logoa','arduraduna','arduraduna__photo').all()
    return render(request, 'joko_itzulpenak/proiektuak.html',locals())
