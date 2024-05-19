from django.urls import re_path
from gamerauntsia.getb import views

urlpatterns = [
    re_path(r"^$", views.index, name="getb_index"),
    re_path(r"^(?P<slug>[-\w]+)$", views.atala, name="getb_atala"),
]
