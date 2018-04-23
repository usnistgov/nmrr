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
        explore_keywords_tile = {
            "logo": "fa-search",
            "link":  reverse("core_explore_keyword_app_search"),
            "title": "Search for resources",
            "text": "Click here to explore the Registry using keywords."
        }

        context["tiles"].append(explore_keywords_tile)

    if "core_curate_app" in installed_apps:
        curate_tile = {
            "logo": "fa-edit",
            "link": reverse("core_curate_index"),
            "title": "Add your resource",
            "text": "Click here to add a new Resource to the Registry."
        }

        context["tiles"].append(curate_tile)

    if not request.user.is_authenticated():
        login_tile = {
            "logo": "fa-sign-in",
            "link": reverse("core_main_app_login"),
            "title": "Login",
            "text": "Click here to login to the Registry."
        }

        context["tiles"].append(login_tile)
    else:
        logout_tile = {
            "logo": "fa-sign-out",
            "link": reverse("core_main_app_logout"),
            "title": "Logout",
            "text": "Click here to logout from the Registry."
        }

        context["tiles"].append(logout_tile)

    return render(request, "nmrr_home/tiles.html", context)
