from gamerauntsia.getb.models import Atala
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import get_object_or_404
from datetime import datetime

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from gamerauntsia.getb.serializers import GetbSerializer
from rest_framework.response import Response
import json
# from django.core import serializers
# from django.core.serializers import serialize
from itertools import chain


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def app_getb_list(request):
    if request.method == 'GET':
        atalak = Atala.objects.all()
        serializer = GetbSerializer(atalak, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def atala_detail(request, pk):
    try:
        atala = Atala.objects.get(pk=pk)
    except Atala.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GetbSerializer(atala)
        return JSONResponse(serializer.data)
    elif request.method == 'HEAD':
        serializer = GetbSerializer(atala)
        return JSONResponse(serializer.data)


def index(request):
    atal_nab = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).order_by('-pub_date')[0]
    atalak = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).exclude(id=atal_nab.id).order_by(
        '-pub_date')
    atalgehiago = atalak[3:7]
    return render_to_response('getb/index.html', locals(), context_instance=RequestContext(request))


def atala(request, slug):
    atala = get_object_or_404(Atala, slug=slug)
    related_atalak = Atala.objects.filter(publikoa_da=True, pub_date__lt=datetime.now()).exclude(id=atala.id).order_by(
        '-pub_date')[:5]
    facebook_id = settings.FACEBOOK_APP_ID
    return render_to_response('getb/atala.html', locals(), context_instance=RequestContext(request))
