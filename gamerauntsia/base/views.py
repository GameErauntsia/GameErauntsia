from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Terminoa

def index(request):
    items = Terminoa.objects.all().order_by('term_eu')
    return render_to_response('base/terminologia.html', locals(),context_instance=RequestContext(request))
