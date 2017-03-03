from gamerauntsia.log.models import Log
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from gamerauntsia.log.serializers import LogSerializer
from rest_framework import viewsets


class DenboralerroaViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-fetxa')
    serializer_class = LogSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def denboralerroa_list(request):
    if request.method == 'GET':
        denboralerroa = Log.objects.all()
        serializer = LogSerializer(denboralerroa, many=True)
        return JSONResponse(serializer.data)


def index(request):
    events = Log.objects.all().order_by('-fetxa')
    return render(request, 'log/index.html', locals())
