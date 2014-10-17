from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import get_object_or_404
from gamerauntsia.aurkezpenak.models import Aurkezpena

def index(request):
    items = Aurkezpena.objects.all()
    return render_to_response('aurkezpenak/index.html', locals(),context_instance=RequestContext(request))

def aurkezpena(request,slug):
    item = get_object_or_404(Aurkezpena,slug=slug)
    return render_to_response('aurkezpenak/'+item.template_name, locals(),context_instance=RequestContext(request))
