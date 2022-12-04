from django import forms
from django_bootstrap_calendar.models import CalendarEvent
from datetimewidget.widgets import DateTimeWidget
from django.utils.translation import ugettext as _

CSS_CLASS_CHOICES = (
    ("event-warning", _("Partida")),
    ("event-info", _("Jokoa")),
    ("event-important", _("Berezia")),
)


class EventForm(forms.ModelForm):

    desc = forms.CharField(label="", widget=forms.Textarea)

    css_class = forms.ChoiceField(label=_("Type"), choices=CSS_CLASS_CHOICES)
    start = forms.DateTimeField(
        label=_("Start Date"), widget=DateTimeWidget(usel10n=True, bootstrap_version=3)
    )
    end = forms.DateTimeField(
        label=_("End Date"),
        widget=DateTimeWidget(usel10n=True, bootstrap_version=3),
        required=False,
    )

    class Meta:
        model = CalendarEvent
        fields = "__all__"
