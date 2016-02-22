from gamerauntsia.log.models import Log
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from datetime import datetime
from django.shortcuts import get_object_or_404

def index(request):
    events = Log.objects.all().order_by('-fetxa')
    return render_to_response('log/index.html', locals(),context_instance=RequestContext(request))