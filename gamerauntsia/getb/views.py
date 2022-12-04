from gamerauntsia.getb.models import Atala
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from gamerauntsia.getb.serializers import GetbSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def app_getb_list(request):
    if request.method == "GET":
        atalak = Atala.objects.all()
        serializer = GetbSerializer(atalak, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def atala_detail(request, pk):
    try:
        atala = Atala.objects.get(pk=pk)
    except Atala.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = GetbSerializer(atala)
        return JSONResponse(serializer.data)
    elif request.method == "HEAD":
        serializer = GetbSerializer(atala)
        return JSONResponse(serializer.data)


def index(request):
    atal_nab = Atala.objects.filter(
        publikoa_da=True, pub_date__lt=timezone.now()
    ).order_by("-pub_date")[0]
    atalak = (
        Atala.objects.filter(publikoa_da=True, pub_date__lt=timezone.now())
        .exclude(id=atal_nab.id)
        .order_by("-pub_date")
    )
    atalgehiago = atalak[3:7]
    return render(request, "getb/index.html", locals())


def atala(request, slug):
    atala = get_object_or_404(Atala, slug=slug)
    related_atalak = (
        Atala.objects.filter(publikoa_da=True, pub_date__lt=timezone.now())
        .exclude(id=atala.id)
        .order_by("-pub_date")[:5]
    )
    facebook_id = settings.FB_APP_ID
    return render(request, "getb/atala.html", locals())
