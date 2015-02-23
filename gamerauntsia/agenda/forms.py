from django import forms
from django_bootstrap_calendar.models import CalendarEvent
from django.contrib.admin import widgets

class EventForm(forms.ModelForm):

    class Meta:
        model = CalendarEvent

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget = widgets.AdminSplitDateTime()
        self.fields['end'].widget = widgets.AdminSplitDateTime()