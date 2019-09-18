from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^index/$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<id>\d)$', views.edit, name='edit'),

]
