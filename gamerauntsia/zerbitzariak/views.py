from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import JokuPlataforma
from gamerauntsia.utils.urls import get_urljson

def set_user_whitelist(user,nick=None):
    if user:
        if MC_Whitelist.objects.get(user=user).exists() and nick:
            ml = MC_Whitelist.objects.get(user=user,plataforma='minecraft')
            ml.mc_user = nick
        else:
            if JokuPlataforma.objects.filter(user=user, plataforma='minecraft').exists():
                ml = MC_Whitelist()
                ml.mc_user = JokuPlataforma.objects.filter(user=user, plataforma='minecraft')[0].nick
                ml.user = user

        if ml:
            uuid = get_urljson('https://api.mojang.com/users/profiles/minecraft/'+ml.mc_user)
            if uuid:
                ml.uuid = uuid['id']
            ml.save()
            return True
    return False

def minecraft_server(request):
    user = request.user
    mc_list = MC_Whitelist.objects.all().order_by('-created')[:10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a')
    mc_vip_list = MC_Whitelist.objects.filter(rol='v')
    return render_to_response('zerbitzariak/minecraft.html', locals(),context_instance=RequestContext(request))

def minecraft_add(request):
    user = request.user
    set_user_whitelist(user)
    return HttpResponseRedirect(reverse('minecraft_index'))
