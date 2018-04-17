"""nmrr URL Configuration
"""
from django.conf.urls import url

from nmrr_home import views

urlpatterns = [
    url(r'^tiles', views.tiles, name="nmrr_home_tiles"),
]
