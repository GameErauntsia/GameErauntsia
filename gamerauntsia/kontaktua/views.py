from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.core.mail import send_mail
from django.template import loader
from .forms import ContactForm

def contact_form(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                email_content = loader.render_to_string('kontaktua/email_tmpl.html', {'email': from_email, 'body': message})
                send_mail(settings.EMAIL_SUBJECT + ' ' + subject,
                          email_content,
                          settings.DEFAULT_FROM_EMAIL,
                          [settings.DEFAULT_TO_EMAIL],
                          reply_to=[from_email],
                          fail_silently=False)
            except:
                return render(request, 'kontaktua/index.html', {'form': form})
            return render(request, 'kontaktua/bidalita.html', {})
    return render(request, 'kontaktua/index.html', {'form': form})
