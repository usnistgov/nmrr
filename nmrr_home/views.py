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

    if "core_explore_keyword_app" in installed_apps:
        # TODO: Change URLs once refinements are developed
        keyword_url = reverse("core_explore_keyword_app_search")

        organizations_tile = {
            "logo": "fa-university",
            "color": "#2CAAE2",
            "link":  keyword_url,
            "title": "Organizations",
            "text": "Click here to explore the Organizations."
        }

        context["tiles"].append(organizations_tile)

        data_collections_tile = {
            "logo": "fa-table",
            "color": "#A1C057",
            "link": keyword_url,
            "title": "Data Collections",
            "text": "Click here to explore the Data Collections."
        }

        context["tiles"].append(data_collections_tile)

        datasets_tile = {
            "logo": "fa-database",
            "color": "grey",
            "link": keyword_url,
            "title": "Datasets",
            "text": "Click here to explore the Datasets."
        }

        context["tiles"].append(datasets_tile)

        services_tile = {
            "logo": "fa-cogs",
            "color": "#EBB057;",
            "link": keyword_url,
            "title": "Services",
            "text": "Click here to explore the Services."
        }

        context["tiles"].append(services_tile)

        informational_tile = {
            "logo": "fa-laptop",
            "color": "#257ABC;",
            "link": keyword_url,
            "title": "Informational Sites",
            "text": "Click here to explore the Informational Sites."
        }

        context["tiles"].append(informational_tile)

        software_tile = {
            "logo": "fa-tachometer",
            "color": "#79B320;",
            "link": keyword_url,
            "title": "Software",
            "text": "Click here to explore the Software."
        }

        context["tiles"].append(software_tile)

    return render(request, "nmrr_home/tiles.html", context)
