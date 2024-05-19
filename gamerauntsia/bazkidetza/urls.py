from django.urls import re_path
from gamerauntsia.bazkidetza import views

urlpatterns = [
    re_path(r"^$", views.index, name="bazkidetza"),
    re_path(r"^izan-bazkide/$", views.create_bazkidea, name="create_bazkidea"),
    re_path(
        r"^eskaera-egin/(?P<eskaintza_id>[\d]+)/$",
        views.create_eskaera,
        name="create_eskaera",
    ),
    re_path(r"^ordainketa-eginda/$", views.payment_done, name="payment_done"),
    re_path(r"^eskaintza/(?P<slug>[-\w]+)/$", views.eskaintza, name="eskaintza"),
]
