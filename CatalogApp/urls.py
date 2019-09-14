from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/posDashboard.html'), name="homepage"),
    url(r'^categories/', include(('categories.urls', 'categories'), namespace='categories')),
]
