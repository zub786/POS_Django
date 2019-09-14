from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/homepage.html'), name="homepage"),
    # url('', admin.site.urls),
    # path('admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^about/', include(('cofeehouse.about.urls', 'about'),  namespace='about')),
    # url(r'^stores/', include(('cofeehouse.stores.urls', 'stores'), namespace='store')),
    # url(r'^contact/', include(('cofeehouse.contactus.urls', 'contactus'), namespace='contactus')),
    # url(r'^rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
