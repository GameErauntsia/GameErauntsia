from django.conf import settings
import requests

def get_twitch_token():
    response = requests.post("https://id.twitch.tv/oauth2/token",
                             params= {'client_id': settings.STREAMING_TWITCH_CLIENT_ID,
                                      'client_secret': settings.STREAMING_TWITCH_CLIENT_SECRET,
                                      'grant_type':'client_credentials'})
    token = response.json()['access_token']
    return token

def get_stream_info(user_id):
    token = get_twitch_token()
    response = requests.get("https://api.twitch.tv/helix/channels",
                            params={'broadcaster_id':user_id},
                            headers={'Authorization': 'Bearer ' + token,
                                     'Client-ID': settings.STREAMING_TWITCH_CLIENT_ID})
    return response.json()['data'][0]

def get_twitch_user_id(token, user_name):
    try:
        response = requests.get("https://api.twitch.tv/helix/users",
                                params={'login':user_name},
                                headers={'Authorization': 'Bearer ' + token,
                                         'Client-ID': settings.STREAMING_TWITCH_CLIENT_ID})
        return response.json()['data'][0]['id']
    except:
        return None

def create_twitch_subscription(token, user_id, sub_type):
    try:
        response = requests.post("https://api.twitch.tv/helix/eventsub/subscriptions",
                                 headers={'Authorization': 'Bearer ' + token,
                                          'Client-ID': settings.STREAMING_TWITCH_CLIENT_ID},
                                 json={'type': sub_type,
                                       'version': 1,
                                       'condition': {'broadcaster_user_id': user_id},
                                       'transport': {'method': 'webhook',
                                                     'callback': 'https://gamerauntsia.eus/streaming/twitch-callback',
                                                     'secret': settings.STREAMING_TWITCH_WEBHOOK_SECRET}})
        return response.json()['data'][0]['id']
    except:
        return None

def delete_twitch_subscription(token, subscription_id):
    try:
        response = requests.delete("https://api.twitch.tv/helix/eventsub/subscriptions",
                                   params={'id':subscription_id},
                                   headers={'Authorization': 'Bearer ' + token,
                                            'Client-ID': settings.STREAMING_TWITCH_CLIENT_ID})
        return True
    except:
        return None
