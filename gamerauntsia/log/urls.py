from django.conf.urls import url
from gamerauntsia.log import views
from gamerauntsia.jokoa import views as gameviews

urlpatterns = [
    url(r'^$', views.index, name='log_index'),
    url(r'^(?P<slug>[-\w]+)$', gameviews.jokoa, name='game'),
]
