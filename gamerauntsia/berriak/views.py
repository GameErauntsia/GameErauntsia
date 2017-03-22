from datetime import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import RequestContext
from gamerauntsia.berriak.models import Berria, Gaia
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from gamerauntsia.berriak.serializers import BerriaSerializer
from rest_framework import viewsets


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class BerriaViewSet(viewsets.ModelViewSet):
    queryset = Berria.objects.all()
    serializer_class = BerriaSerializer


class BerriadetailViewSet(viewsets.ModelViewSet):
    queryset = Berria.objects.all()
    serializer_class = BerriaSerializer


# @csrf_exempt
# def app_berria_list(request):
#     if request.method == 'GET':
#         berriak = Berria.objects.all()
#         serializer = BerriaSerializer(berriak, many=True)
#         return JSONResponse(serializer.data)
# 		paginator = PageNumberPagination()
#         page = paginator.paginate_queryset(berriak, request)
#         serializer = BerriaSerializer(page, many=True, context={'request': request})
#         return paginator.get_paginated_response(serializer.data)
@csrf_exempt
def berria_detail(request, pk):
    try:
        b = Berria.objects.get(pk=pk)
    except Berria.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BerriaSerializer(b)
        return JSONResponse(serializer.data)
    elif request.method == 'HEAD':
        serializer = BerriaSerializer(b)
        return JSONResponse(serializer.data)


def index(request):
    h = {}
    zerr_berriak = Berria.objects.filter(status='1', pub_date__lt=datetime.now()).order_by('-pub_date')
    return render(request, 'berriak/index.html', locals())


def berria(request, slug):
    item = get_object_or_404(Berria, slug=slug)
    facebook_id = settings.FB_APP_ID
    return render(request, 'berriak/berria.html', locals())


def gaia(request, slug):
    gaia = get_object_or_404(Gaia, slug=slug)
    zerr_berriak = Berria.objects.filter(gaia=gaia, status='1', pub_date__lt=datetime.now()).order_by('-pub_date')
    return render(request, 'berriak/gaia.html', locals())
