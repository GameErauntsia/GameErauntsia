from django.shortcuts import render
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import JokuPlataforma
from gamerauntsia.utils.urls import get_urljson
from .forms import MCForm


def set_user_whitelist(user, nick, action=None):
    if user and nick:
        ml = None
        if MC_Whitelist.objects.filter(user=user).exists():
            ml = MC_Whitelist.objects.get(user=user)
        else:
            ml = MC_Whitelist()
            ml.user = user
        ml.mc_user = nick

        if action == 'edit':
            jp = JokuPlataforma.objects.get(user=user, plataforma='minecraft')
            jp.nick = nick
            jp.save()
        elif not JokuPlataforma.objects.filter(user=user, plataforma='minecraft', nick=nick).exists():
            jp = JokuPlataforma(user=user, plataforma='minecraft', nick=nick)
            jp.save()

        if ml:
            uuid = get_urljson('https://api.mojang.com/users/profiles/minecraft/' + ml.mc_user)
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
    mc_form = MCForm()
    carousel_images = range(1,21)
    return render(request, 'zerbitzariak/minecraft.html', locals())


def minecraft_mapa(request):
    user = request.user
    mc_list = MC_Whitelist.objects.all().order_by('-created')[:10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a')
    mc_vip_list = MC_Whitelist.objects.filter(rol='v')
    return render(request, 'zerbitzariak/minecraft_mapa.html', locals())


def minecraft_add(request):
    mc_list = MC_Whitelist.objects.all().order_by('-created')[:10]
    mc_admin_list = MC_Whitelist.objects.filter(rol='a')
    mc_vip_list = MC_Whitelist.objects.filter(rol='v')
    if request.POST:
        if request.method == 'POST':
            mcform = MCForm(request.POST)
            if mcform.is_valid():
                nick = mcform.cleaned_data['mc_user']
                user = request.user
                set_user_whitelist(user, nick)
    return render(request, 'zerbitzariak/minecraft.html', locals())
