from gamerauntsia.bazkidetza.models import Eskaintza, Bazkidea, Eskaera
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q


def index(request):
    if request.user.is_authenticated:
        bazkidea = request.user.get_bazkidea()
    eskaintzak = Eskaintza.objects.filter(
        Q(is_public=True),
        Q(expire_date__gte=timezone.now()) | Q(expire_date__isnull=True),
    ).order_by("-activate_date")
    return render(request, "bazkidetza/index.html", locals())


def eskaintza(request, slug):
    if request.user.is_authenticated:
        bazkidea = request.user.get_bazkidea()
    eskaintza = get_object_or_404(Eskaintza, slug=slug, is_public=True)
    return render(request, "bazkidetza/eskaintza.html", locals())


def create_bazkidea(request):
    if not Bazkidea.objects.filter(user=request.user).exists():
        bazkide = Bazkidea(user=request.user, is_active=True)
        bazkide.save()
    return HttpResponseRedirect(reverse("bazkidetza"))


def create_eskaera(request, eskaintza_id):
    if (
        request.user.is_authenticated
        and Bazkidea.objects.filter(user=request.user).exists()
    ):
        eskaintza = Eskaintza.objects.get(id=eskaintza_id)
        bazkidea = Bazkidea.objects.get(user=request.user)
        eskaera = Eskaera(eskaintza=eskaintza, bazkidea=bazkidea)
        eskaera.save()
    return HttpResponseRedirect(reverse("bazkidetza"))


def payment_done(request):
    if (
        request.user.is_authenticated
        and Bazkidea.objects.filter(user=request.user).exists()
    ):
        bazkide = Bazkidea.objects.get(user=request.user)
        bazkide.paid = True
        bazkide.expire_date = timezone.localtime(
            timezone.now().replace(year=timezone.now().year + 1)
        )
        bazkide.save()
    return HttpResponseRedirect(reverse("bazkidetza"))
