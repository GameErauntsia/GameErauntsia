from django.conf import settings

def fb_app_id(request):
    return {'FB_APP_ID': settings.FB_APP_ID}

def enable_tracking(request):
    print(settings.ENABLE_TRACKING)
    return {'ENABLE_TRACKING': settings.ENABLE_TRACKING}
