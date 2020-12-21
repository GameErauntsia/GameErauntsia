from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, renderer_classes, permission_classes
import hmac
import hashlib

def valid_twitch_signature(request):
    try:
        message_id = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_ID']
        message_timestamp = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_TIMESTAMP']
        hmac_message = bytes(message_id,'utf-8') + bytes(message_timestamp,'utf-8') + request.body
        signature = hmac.new(settings.STREAMING_TWITCH_WEBHOOK_SECRET,
                             hmac_message,
                             hashlib.sha256)
        expected_signature_header = 'sha256=' + signature.hexdigest()
        got_signature_header = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_SIGNATURE']
        return hmac.compare_digest(expected_signature_header,got_signature_header)
    except Exception as e:
        return False

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def twitch_subscription_callback(request, format=None):
    if valid_twitch_signature(request):
        message_type = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_TYPE']
        if message_type == "webhook_callback_verification":
            challenge = request.data["challenge"]
            print(request.data)
            return HttpResponse(challenge,content_type='text/plain')
        else:
            event = request.data['event']
            print(event)
            return HttpResponse()
    else:
        return Response(status=403)
