from django.shortcuts import render
from django.shortcuts import get_object_or_404
from gamerauntsia.aurkezpenak.models import Aurkezpena


def index(request):
    items = Aurkezpena.objects.all()
    return render(request, 'aurkezpenak/index.html', locals())


def aurkezpena(request, slug):
    item = get_object_or_404(Aurkezpena, slug=slug)
    return render(request, 'aurkezpenak/presentation.html', locals())
