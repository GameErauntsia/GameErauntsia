from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

def bilaketa(request,bilatu):
    h = {}
    try:
        h['q'] = bilatu
    except:
        raise Http404 
    return render_to_response('bilaketa.html', h,context_instance=RequestContext(request))
