from django import forms
from django_bootstrap_calendar.models import CalendarEvent

class EventForm(forms.ModelForm):

    class Meta:
        model = CalendarEvent