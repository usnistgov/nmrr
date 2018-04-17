from django.core.urlresolvers import reverse
from django.shortcuts import render


def tiles(request):
    """

    :param request:
    :return:
    """
    from django.conf import settings
    installed_apps = settings.INSTALLED_APPS

    context = {
        "tiles": []
    }

    if "core_curate_app" in installed_apps:
        curate_tile = {
            "logo": "fa-edit",
            "link": reverse("core_curate_index"),
            "title": "Curate your Materials Data",
            "text": "Click here to select a form template and then fill out the corresponding form."
        }

        context["tiles"].append(curate_tile)

    if "core_explore_example_app" in installed_apps:
        explore_example_tile = {
            "logo": "fa-flask",
            "link":  reverse("core_explore_example_index"),
            "title": "Build your own queries",
            "text": "Click here to search for Materials Data in the repository using flexible queries."
        }

        context["tiles"].append(explore_example_tile)

    if "core_explore_keyword_app" in installed_apps:
        explore_keywords_tile = {
            "logo": "fa-search",
            "link":  reverse("core_explore_keyword_app_search"),
            "title": "Search by keyword",
            "text": "Click here to explore for Materials Data in the repository using keywords."
        }

        context["tiles"].append(explore_keywords_tile)

    return render(request, "nmrr_home/tiles.html", context)
