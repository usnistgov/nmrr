"""nmrr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from core_parser_app.tools.modules.discover import discover_modules

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/defender/', include('defender.urls')),
    re_path(r'^', include("core_main_registry_app.urls")),
    re_path(r'^home/', include("nmrr_home.urls")),
    re_path(r'^', include("core_website_app.urls")),
    re_path(r'^curate/', include("core_curate_registry_app.urls")),
    re_path(r'^parser/', include("core_parser_app.urls")),
    re_path(r'^explore/common/', include("core_explore_common_app.urls")),
    re_path(r'^explore/keyword/', include("core_explore_keyword_registry_app.urls")),
    re_path(r'^oaipmh_search/', include("core_explore_oaipmh_app.urls")),
    re_path(r'^dashboard/', include("core_dashboard_registry_app.urls")),
    re_path(r'^oai_pmh/', include("core_oaipmh_harvester_app.urls")),
    re_path(r'^oai_pmh/server/', include("core_oaipmh_provider_app.urls")),
    re_path(r'^', include('core_module_local_id_registry_app.urls')),
    re_path(r'^', include('core_module_status_registry_app.urls')),
    re_path(r'^', include('core_module_fancy_tree_registry_app.urls')),
    re_path(r'^', include('core_module_text_area_app.urls')),
]

# TODO: see if we can automate the discovery and run it from parser app
discover_modules(urlpatterns)
