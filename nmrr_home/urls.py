"""nmrr URL Configuration
"""

from django.urls import re_path

from nmrr_home import views

urlpatterns = [
    re_path(r'^tiles', views.tiles, name="nmrr_home_tiles"),
]
