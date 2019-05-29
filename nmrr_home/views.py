from builtins import str
import logging

from django.shortcuts import render
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
            "user_id": query.user_id
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
            get_categories = category_api.get_all_categories_ids_by_parent_slug_and_refinement_id
            organizations_tile = {
                "logo": "fa-university",
                "color": "#2CAAE2",
                "categories":  get_categories('organization', refinement.id),
                "title": "Organizations",
                "text": "Click here to explore the Organizations."
            }

            context["tiles"].append(organizations_tile)

            data_collections_tile = {
                "logo": "fa-table",
                "color": "#A1C057",
                "categories":  get_categories('collection', refinement.id),
                "title": "Data Collections",
                "text": "Click here to explore the Data Collections."
            }

            context["tiles"].append(data_collections_tile)

            datasets_tile = {
                "logo": "fa-database",
                "color": "grey",
                "categories":  get_categories('dataset', refinement.id),
                "title": "Datasets",
                "text": "Click here to explore the Datasets."
            }

            context["tiles"].append(datasets_tile)

            services_tile = {
                "logo": "fa-cogs",
                "color": "#EBB057;",
                "categories":  get_categories('service', refinement.id),
                "title": "Services",
                "text": "Click here to explore the Services."
            }

            context["tiles"].append(services_tile)

            informational_tile = {
                "logo": "fa-laptop",
                "color": "#257ABC;",
                "categories":  get_categories('web-site', refinement.id),
                "title": "Informational Sites",
                "text": "Click here to explore the Informational Sites."
            }

            context["tiles"].append(informational_tile)

            software_tile = {
                "logo": "fa-tachometer",
                "color": "#79B320;",
                "categories":  get_categories('software', refinement.id),
                "title": "Software",
                "text": "Click here to explore the Software."
            }

            context["tiles"].append(software_tile)
        except (exceptions.DoesNotExist, exceptions.ModelError) as e:
            logger.error("Error while getting information from the database: {0}".format(str(e)))
        except Exception as ex:
            logger.error("Something wrong occurred during the tiles "
                         "generation: {0}".format(str(ex)))

    return render(request, "nmrr_home/tiles.html", context)
