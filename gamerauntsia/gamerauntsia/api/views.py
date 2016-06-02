import telebot
from django.conf import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from gamerauntsia.zerbitzariak.models import MC_Whitelist


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def mc_whitelist(request, format=None):
    
    base = MC_Whitelist.objects
    username = request.GET.get("username","") 
    uuid = request.GET.get("uuid","")
    
    if username:
        try:
            mc = base.get(mc_user=username)
            data = {
               'user': mc.user.username,
               'mc_user': mc.mc_user,
               'created': mc.created.strftime("%Y-%m-%d %H:%M:%S"),
               'rol': mc.get_rol_display(),
               'uuid': mc.uuid != '' and mc.uuid or None,
            }
            return Response(data)
        except:
            return Response(False)
    elif uuid:
        try:
            mc = base.get(uuid=uuid)
            data = {
               'user': mc.user.username,
               'mc_user': mc.mc_user,
               'created': mc.created.strftime("%Y-%m-%d %H:%M:%S"),
               'rol': mc.get_rol_display(),
               'uuid': mc.uuid != '' and mc.uuid or None,
            }
            return Response(data)
        except:
            return Response(False)
    else:
        return Response(False)



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def mc_telebot(request, username, format=None):                  
    base = MC_Whitelist.objects
    
    if username:
        try:
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            if base.filter(mc_user=username).exists():
                mc = base.get(mc_user=username)
                msg = '[%s] %s-(r)en laguntza eskaera:\n%s' % (mc.get_rol_display(),username,request.GET.get('text', 'Mezurik gabe...'))
            else:
                msg = '[Anonimoa] %s-(r)en laguntza eskaera:\n%s' % (username,request.GET.get('text', 'Mezurik gabe...'))
            tb.send_message(settings.MC_CHAT_ID, msg)
            return Response(True)
        except:
            return Response(False)
    else:
        return Response(username)
