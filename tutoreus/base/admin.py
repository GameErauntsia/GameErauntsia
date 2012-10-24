from base.models import Base
from django.contrib import admin
from base.forms import BaseAdminForm
    
class BaseAdmin(admin.ModelAdmin):
    list_display = ('izenburua','azpi_izenburua')
    form = BaseAdminForm
    
admin.site.register(Base, BaseAdmin)