from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import JokuPlataforma

def minecraft_server(request):
    user = request.user
    return render_to_response('zerbitzariak/minecraft.html', locals(),context_instance=RequestContext(request))

def minecraft_add(request):
	user = request.user
	if user:
		if JokuPlataforma.objects.filter(user=user, plataforma='minecraft').exists():
			wl = MC_Whitelist()
			wl.mc_user = JokuPlataforma.objects.filter(user=user, plataforma='minecraft')[0].nick
			wl.user = user
			wl.save()
	return HttpResponseRedirect(reverse('minecraft_index'))