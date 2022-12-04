from django.conf.urls import url
from gamerauntsia.getb import views

urlpatterns = [
    url(r"^$", views.index, name="getb_index"),
    url(r"^(?P<slug>[-\w]+)$", views.atala, name="getb_atala"),
]
