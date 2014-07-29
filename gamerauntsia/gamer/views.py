from gamerauntsia.gamer.models import GamerUser as User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404

def index(request):
    users = User.objects.all()
    return render_to_response('gamer/index.html', locals(),context_instance=RequestContext(request))
    
def profile(request,username):
    user = get_object_or_404(User,username=username)
    return render_to_response('gamer/profile.html', locals(),context_instance=RequestContext(request))
