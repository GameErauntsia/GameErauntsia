from django.conf import settings
from gamerauntsia.berriak.models import Berria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.template import loader

def index(request):
    h = {}
    h['berriak'] = Berria.objects.all().order_by('-pub_date')[:5]
    return render_to_response('kontaktua/index.html', h,context_instance=RequestContext(request))

def bidali(request):
    h = {}
    eposta = request.POST.get('eposta')
    gaia = request.POST.get('gaia')
    iruzkina = request.POST.get('iruzkina')
    tmpl = loader.render_to_string('kontaktua/email_tmpl.html',{'email':eposta,'body': iruzkina})
    send_mail(settings.EMAIL_SUBJECT+' '+gaia, tmpl, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_TO_EMAIL], fail_silently=False)
    h['berriak'] = Berria.objects.all().order_by('-pub_date')[:5]
    return render_to_response('kontaktua/bidalita.html', h,context_instance=RequestContext(request))
