from django.conf.urls import url
from gamerauntsia.bazkidetza import views

urlpatterns = [
    url(r"^$", views.index, name="bazkidetza"),
    url(r"^izan-bazkide/$", views.create_bazkidea, name="create_bazkidea"),
    url(
        r"^eskaera-egin/(?P<eskaintza_id>[\d]+)/$",
        views.create_eskaera,
        name="create_eskaera",
    ),
    url(r"^ordainketa-eginda/$", views.payment_done, name="payment_done"),
    url(r"^eskaintza/(?P<slug>[-\w]+)/$", views.eskaintza, name="eskaintza"),
]
