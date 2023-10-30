from django.conf.urls import url
from gamerauntsia.berriak import views

urlpatterns = [
    url(r"^$", views.index, name="berriak_index"),
    url(r"^gaia/(?P<slug>[-\w]+)/$", views.gaia, name="gaia"),
    url(r"^jokoa/(?P<slug>[-\w]+)/$", views.jokoa, name="jokoa"),
    url(r"^(?P<slug>[-\w]+)/$", views.berria, name="berria"),
]
