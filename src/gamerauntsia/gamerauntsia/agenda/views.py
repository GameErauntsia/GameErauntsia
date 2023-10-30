from django.shortcuts import render
from datetime import datetime
from django_bootstrap_calendar.models import CalendarEvent


def index(request):
    events = CalendarEvent.objects.filter(start__gt=datetime.now()).order_by("start")[
        :10
    ]
    return render(request, "agenda/index.html", locals())
