from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.template import loader
from .forms import ContactForm

def index(request):
    h = {}
    form = ContactForm()
    return render_to_response('kontaktua/index.html', locals(),context_instance=RequestContext(request))

def bidali(request):
    h = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            eposta = request.POST.get('eposta')
            gaia = request.POST.get('gaia')
            iruzkina = request.POST.get('iruzkina')
            tmpl = loader.render_to_string('kontaktua/email_tmpl.html',{'email':eposta,'body': iruzkina})
            send_mail(settings.EMAIL_SUBJECT+' '+gaia, tmpl, settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_TO_EMAIL], fail_silently=False)
            return render_to_response('kontaktua/bidalita.html', h,context_instance=RequestContext(request))
        return HttpResponseRedirect(reverse('kontaktua'))
    return render_to_response('kontaktua/index.html', locals(), context_instance=RequestContext(request))
