from django.conf.urls import url
from gamerauntsia.agenda import views

urlpatterns = [
    url(r'^$', views.index, name='agenda_index'),
]
