from gamerauntsia.finished.models import Finished
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from datetime import datetime
from django.shortcuts import get_object_or_404

def add_finished(request):
    """ """
    user = request.user
    if request.method == 'POST':
        eventform = EventForm(request.POST)
        if eventform.is_valid():
            eventform.save()
            return HttpResponseRedirect(reverse('agenda_index'))

    else:
        eventform = EventForm()
    return render_to_response('profile/add_event.html', locals(), context_instance=RequestContext(request))
