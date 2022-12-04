from django.conf.urls import url
from gamerauntsia.aurkezpenak import views

urlpatterns = [
    url(r"^$", views.index, name="aurkezpenak_index"),
    url(r"^(?P<slug>[-\w]+)$", views.aurkezpena, name="aurkezpena"),
]
