from gamerauntsia.gamer.models import GamerUser
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.conf import settings

def index(request):
    users = GamerUser.objects.all()
    return render_to_response('gamer/index.html', locals(),context_instance=RequestContext(request))
    
def profile(request,username):
    user = get_object_or_404(GamerUser,username=username)
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))
