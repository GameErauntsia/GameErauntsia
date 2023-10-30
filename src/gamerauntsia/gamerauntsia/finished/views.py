from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from gamerauntsia.agenda.forms import EventForm


def add_finished(request):
    """ """
    user = request.user
    if request.method == "POST":
        eventform = EventForm(request.POST)
        if eventform.is_valid():
            eventform.save()
            return HttpResponseRedirect(reverse("agenda_index"))

    else:
        eventform = EventForm()
    return render(request, "profile/add_event.html", locals())
