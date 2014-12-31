from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import JokuPlataforma

def minecraft_server(request):
    user = request.user
    mc_list = MC_Whitelist.objects.all().order_by('-created').values('user')[10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a').values('user')
    mc_vip_list = MC_Whitelist.objects.filter(rol='v').values('user')
    return render_to_response('zerbitzariak/minecraft.html', locals(),context_instance=RequestContext(request))

def minecraft_add(request):
    user = request.user
    if user:
        if JokuPlataforma.objects.filter(user=user, plataforma='minecraft').exists():
            ml = MC_Whitelist()
            ml.mc_user = JokuPlataforma.objects.filter(user=user, plataforma='minecraft')[0].nick
            ml.user = user
            ml.save()
    return HttpResponseRedirect(reverse('minecraft_index'))