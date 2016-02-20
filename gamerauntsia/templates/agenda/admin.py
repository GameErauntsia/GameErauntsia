from models import CalendarEvent
from django.contrib import admin


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title','css_class','url','start','end','all_day')
    ordering = ('-start',)


admin.site.register(CalendarEvent, CalendarEventAdmin)