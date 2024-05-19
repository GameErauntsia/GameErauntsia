from django.urls import re_path
from gamerauntsia.joko_itzulpenak import views

urlpatterns = [
    re_path(r"^proiektuak$", views.itzulpen_proiektuak),
    re_path(
        r"^proiektuak/(?P<slug>[-\w]+)$",
        views.itzulpen_proiektua,
        name="itzulpen_proiektua",
    ),
]
