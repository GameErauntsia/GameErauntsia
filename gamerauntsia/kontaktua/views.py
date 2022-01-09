from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.core.mail import send_mail, EmailMessage
from django.template import loader
from .forms import ContactForm

import logging
logger = logging.getLogger(__name__)

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
                email_body = loader.render_to_string('kontaktua/email_tmpl.html', {'email': from_email, 'body': message})
                email = EmailMessage(settings.EMAIL_SUBJECT + ' ' + subject,
                                     email_body,
                                     from_email=settings.DEFAULT_FROM_EMAIL,
                                     to=[settings.DEFAULT_TO_EMAIL],
                                     reply_to=[from_email])
                result = email.send(fail_silently=False)
                if result == 1:
                    return render(request, 'kontaktua/bidalita.html', {})
                else:
                    logger.error("Could not send contact email")
            except:
                logger.exception("Could not send contact email")
    return render(request, 'kontaktua/index.html', {'form': form})
