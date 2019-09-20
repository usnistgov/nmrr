import logging

from django.shortcuts import render

from nmrr.settings import DATA_SORTING_FIELDS

logger = logging.getLogger(__name__)


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

    if "core_explore_keyword_registry_app" in installed_apps:
        from core_explore_keyword_registry_app.views.user.forms import RefinementForm
        from core_explore_common_app.components.query import api as query_api
        from core_explore_common_app.components.query.models import Query
        from core_explore_common_app.views.user.ajax import add_local_data_source
        from core_main_registry_app.components.refinement import api as refinement_api
        from core_main_registry_app.components.category import api as category_api
        from core_main_registry_app.components.template import api as template_registry_api
        from core_main_registry_app.components.custom_resource import api as custom_resource_api
        from core_main_app.commons import exceptions as exceptions

        # create Query
        query = Query(user_id=str(request.user.id), templates=[])

        # add local data source to the query
        add_local_data_source(request, query)

        # set visibility
        query_api.set_visibility_to_query(query)

        # upsert the query
        query_api.upsert(query)

        # add information in context to populate keyword form
        context.update({
            "query_id": str(query.id),
            "user_id": query.user_id,
            'order_by_field': ','.join(DATA_SORTING_FIELDS),
        })

        try:
            # Get current template
            template = template_registry_api.get_current_registry_template()
            # Get type refinement
            refinement = refinement_api.get_by_template_hash_and_by_slug(template_hash=template.hash,
                                                                         slug='type')
            # Refinement form ID
            refinement_form_id = "{0}-{1}".format(RefinementForm.prefix, refinement.slug)
            context["refinement_form_id"] = refinement_form_id
            # Shorter api name
            get_categories = category_api.get_all_categories_ids_from_name_and_refinement_id

            custom_resources = custom_resource_api.get_all_of_current_template().order_by('sort')

            for custom_resource in custom_resources:
                if custom_resource.display_icon and custom_resource.role_type is not None:
                    tile = {
                        "logo": custom_resource.icon,
                        "color": custom_resource.icon_color,
                        "categories": get_categories(custom_resource.role_type.split(':')[0], refinement.id),
                        "title": custom_resource.title,
                        "text": "Click here to explore the {0}.".format(custom_resource.title)
                    }
                    context["tiles"].append(tile)

        except (exceptions.DoesNotExist, exceptions.ModelError) as e:
            logger.error("Error while getting information from the database: {0}".format(str(e)))
        except Exception as ex:
            logger.error("Something wrong occurred during the tiles "
                         "generation: {0}".format(str(ex)))

    return render(request, "nmrr_home/tiles.html", context)
