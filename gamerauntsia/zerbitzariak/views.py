from django.shortcuts import render, redirect
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import JokuPlataforma
from gamerauntsia.utils.urls import get_urljson
from mcstatus import MinecraftServer
from .forms import MCForm
import re


def minecraft_server(request):
    user = request.user
    mc_list = MC_Whitelist.objects.all().order_by('-created')[:10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a')
    mc_form = MCForm()
    carousel_images = range(1,21)
    return render(request, 'zerbitzariak/minecraft.html', locals())

def get_mc_version_string(mc_server_status):
    try:
        long_version = mc_server_status.version.name
        short_version = re.findall('[0-9]+\.[0-9]+\.[0-9]+',long_version)[0]
        return short_version
    except:
        return None

def minecraft_status(request):
    try:
        mc_server = MinecraftServer.lookup("mc.gamerauntsia.eus")
        mc_server_status = mc_server.status()
        mc_server_version = get_mc_version_string(mc_server_status)
    except:
        mc_server = None
    return render(request, 'zerbitzariak/minecraft_status.html', locals())

def minecraft_mapa(request):
    user = request.user
    mc_list = MC_Whitelist.objects.all().order_by('-created')[:10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a')
    mc_vip_list = MC_Whitelist.objects.filter(rol='v')
    return render(request, 'zerbitzariak/minecraft_mapa.html', locals())


def minecraft_add(request):
    if request.POST and request.method == 'POST':
        mcform = MCForm(request.POST)
        if mcform.is_valid():
            form_data = mcform.cleaned_data
            nick = form_data['mc_user']
            platform = form_data['platform']
            user = request.user

            if not JokuPlataforma.objects.filter(user=user, plataforma=platform, nick=nick).exists():
                jp = JokuPlataforma(user=user, plataforma=platform, nick=nick)
                jp.save()

            ml = MC_Whitelist(user=user)
            ml.save()

    return redirect(minecraft_server)
