import telebot
from django.conf import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from gamerauntsia.zerbitzariak.models import MC_Whitelist
from gamerauntsia.gamer.models import GamerUser

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def mc_whitelist(request, format=None):
    username = request.query_params.get("username")
    edition = request.query_params.get("edition")
    if not username:
        return Response(status=400)
    else:
        try:
            platform_name = 'minecraft_bedrock' if edition == 'bedrock' else 'minecraft'
            query = MC_Whitelist.objects.get(user__plataforma__nick=username,
                                             user__plataforma__plataforma=platform_name)
            data = {'user': query.user.username,
                    'created': query.created.strftime("%Y-%m-%d %H:%M:%S"),
                    'role': query.get_rol_display()}
            return Response(data)
        except:
            return Response(status=404)

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def mc_telebot(request, username, format=None):
    if username:
        try:
            msg = '%s-(r)en laguntza eskaera:\n%s' % (username,request.GET.get('text', 'Mezurik gabe...'))
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            tb.send_message(settings.MC_CHAT_ID, msg)
            return Response(True)
        except:
            return Response(False)
    else:
        return Response(username)
