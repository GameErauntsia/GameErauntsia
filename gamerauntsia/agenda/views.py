from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from django_bootstrap_calendar.models import CalendarEvent


def index(request):
    events = CalendarEvent.objects.filter(start__lt=datetime.now())[:10]
    return render_to_response('agenda/index.html', locals(),context_instance=RequestContext(request))

