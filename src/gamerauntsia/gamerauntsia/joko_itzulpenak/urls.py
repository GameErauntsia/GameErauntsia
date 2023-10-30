from django.conf.urls import url
from gamerauntsia.joko_itzulpenak import views

urlpatterns = [
    url(r"^proiektuak$", views.itzulpen_proiektuak),
    url(
        r"^proiektuak/(?P<slug>[-\w]+)$",
        views.itzulpen_proiektua,
        name="itzulpen_proiektua",
    ),
]
