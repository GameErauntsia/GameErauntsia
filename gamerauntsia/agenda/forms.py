from django import forms
from django_bootstrap_calendar.models import CalendarEvent
from datetimewidget.widgets import DateTimeWidget

class EventForm(forms.ModelForm):

    start_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    end_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    class Meta:
        model = CalendarEvent