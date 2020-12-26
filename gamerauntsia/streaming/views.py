from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from gamerauntsia.utils.urls import get_urljson
from gamerauntsia.gamer.models import GamerUser
from gamerauntsia.streaming.models import Streaming
from gamerauntsia.streaming.twitch_api import get_stream_info
from django.utils import timezone
from django.shortcuts import render
from django.http import Http404
import telebot
import hmac
import hashlib
import logging
logger = logging.getLogger(__name__)

def valid_twitch_signature(request):
    try:
        message_id = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_ID']
        message_timestamp = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_TIMESTAMP']
        hmac_message = bytes(message_id,'utf-8') + bytes(message_timestamp,'utf-8') + request.body
        key = bytes(settings.STREAMING_TWITCH_WEBHOOK_SECRET, 'utf-8')
        signature = hmac.new(key,
                             hmac_message,
                             hashlib.sha256)
        expected_signature_header = 'sha256=' + signature.hexdigest()
        got_signature_header = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_SIGNATURE']
        return hmac.compare_digest(expected_signature_header,got_signature_header)
    except Exception as e:
        logger.info('Invalid Twitch callback signature')
        return False

def streaming_started(event):
    try:
        user_id = event['broadcaster_user_id']
        channel_info = get_stream_info(user_id)
        if channel_info:
            user = GamerUser.objects.filter(twitch_channel_id=user_id).first()
            streaming = Streaming(title=channel_info['title'],
                                  twitch_id=event['id'],
                                  user=user,
                                  game_name=channel_info['game_name'])
            streaming.save()
            tb = telebot.TeleBot(settings.TELEBOT_TOKEN)
            if channel_info['title']:
                msg = "%s %s (%s) stremeatzen ari da! https://twitch.tv/%s" % (channel_info['broadcaster_name'],
                                                                               channel_info['title'],
                                                                               channel_info['game_name'],
                                                                               channel_info['broadcaster_name'])
            else:
                msg = "%s %s stremeatzen ari da! https://twitch.tv/%s" % (channel_info['broadcaster_name'],
                                                                          channel_info['game_name'],
                                                                          channel_info['broadcaster_name'])
            tb.send_message(settings.PUBLIC_CHAT_ID, msg)
    except:
        logger.error('Could not create stream: ' + str(event))

def streaming_ended(event):
    try:
        user_id = event['broadcaster_user_id']
        user = GamerUser.objects.filter(twitch_channel_id=user_id).first()
        Streaming.objects.filter(user=user,end_date=None).update(end_date=timezone.now())
    except:
        logger.error('Could not end stream: ' + str(event))

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
@permission_classes((AllowAny,))
def twitch_subscription_callback(request, format=None):
    if valid_twitch_signature(request):
        message_type = request.META['HTTP_TWITCH_EVENTSUB_MESSAGE_TYPE']
        if message_type == "webhook_callback_verification":
            challenge = request.data["challenge"]
            return HttpResponse(challenge,content_type='text/plain')
        else:
            notification_type = request.data['subscription']['type']
            user_id = request.data['event']['broadcaster_user_id']
            event = request.data['event']
            if notification_type == "stream.online":
                streaming_started(event)
            elif notification_type == "stream.offline":
                streaming_ended(event)
            return HttpResponse()
    else:
        return Response(status=403)

def streaming(request, slug, related=None):
    streamer = GamerUser.objects.filter(twitch_channel=slug).first()
    if not streamer:
        raise Http404
    streaming = Streaming.objects.filter(user=streamer,end_date=None).first()
    return render(request, 'streaming/streaming.html', locals())
