from django.urls import re_path
from gamerauntsia.berriak import views

urlpatterns = [
    re_path(r"^$", views.index, name="berriak_index"),
    re_path(r"^gaia/(?P<slug>[-\w]+)/$", views.gaia, name="gaia"),
    re_path(r"^jokoa/(?P<slug>[-\w]+)/$", views.jokoa, name="jokoa"),
    re_path(r"^(?P<slug>[-\w]+)/$", views.berria, name="berria"),
]
