from django.urls import re_path
from gamerauntsia.agenda import views

urlpatterns = [
    re_path(r"^$", views.index, name="agenda_index"),
]
