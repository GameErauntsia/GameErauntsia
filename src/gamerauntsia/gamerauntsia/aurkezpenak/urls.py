from django.urls import re_path
from gamerauntsia.aurkezpenak import views

urlpatterns = [
    re_path(r"^$", views.index, name="aurkezpenak_index"),
    re_path(r"^(?P<slug>[-\w]+)$", views.aurkezpena, name="aurkezpena"),
]
