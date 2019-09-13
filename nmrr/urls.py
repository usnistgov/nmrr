"""nmrr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core_parser_app.tools.modules.discover import discover_modules

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/defender/', include('defender.urls')),
    url(r'^', include("core_main_registry_app.urls")),
    url(r'^home/', include("nmrr_home.urls")),
    url(r'^', include("core_website_app.urls")),
    url(r'^curate/', include("core_curate_registry_app.urls")),
    url(r'^parser/', include("core_parser_app.urls")),
    url(r'^explore/common/', include("core_explore_common_app.urls")),
    url(r'^explore/keyword/', include("core_explore_keyword_registry_app.urls")),
    url(r'^oaipmh_search/', include("core_explore_oaipmh_app.urls")),
    url(r'^dashboard/', include("core_dashboard_registry_app.urls")),
    url(r'^oai_pmh/', include("core_oaipmh_harvester_app.urls")),
    url(r'^oai_pmh/server/', include("core_oaipmh_provider_app.urls")),
    url(r'^', include('core_module_local_id_registry_app.urls')),
    url(r'^', include('core_module_status_registry_app.urls')),
    url(r'^', include('core_module_fancy_tree_registry_app.urls')),
    url(r'^', include('core_module_text_area_app.urls')),
]

# TODO: see if we can automate the discovery and run it from parser app
discover_modules(urlpatterns)
