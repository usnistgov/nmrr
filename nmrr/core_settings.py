""" Django settings for core applications.
"""
import os

SERVER_URI = os.environ["SERVER_URI"] if "SERVER_URI" in os.environ else None

# Website customization
WEBSITE_SHORT_TITLE = "NMRR"
CUSTOM_DATA = "Materials Data"
CUSTOM_NAME = os.environ["SERVER_NAME"] if "SERVER_NAME" in os.environ else "NMRR"
CUSTOM_TITLE = "Materials Resource Registry"
CUSTOM_SUBTITLE = "Part of the Materials Genome Initiative"
CURATE_MENU_NAME = "Publish resource"
EXPLORE_MENU_NAME = "Search for resources"
WORKSPACE_DISPLAY_NAME = "workspace"
WEBSITE_ADMIN_COLOR = "blue"
# black, black-light, blue, blue-light, green, green-light, purple, purple-light, red, red-light, yellow, yellow-light

DATA_SOURCES_EXPLORE_APPS = ["core_explore_oaipmh_app"]

# Lists in data not stored if number of elements is over the limit (e.g. 100)
SEARCHABLE_DATA_OCCURRENCES_LIMIT = None
""" integer: Avoid indexing large lists 
"""

PARSER_DOWNLOAD_DEPENDENCIES = True
""" boolean: Does the parser download dependencies
"""

EXPLORE_ADD_DEFAULT_LOCAL_DATA_SOURCE_TO_QUERY = True
""" boolean: Do we add the local data source to new queries by default
"""

SSL_CERTIFICATES_DIR = True
""" Either a boolean, in which case it controls whether requests verify the server's TLS certificate, 
or a string, in which case it must be a path to a CA bundle to use.
"""

XSD_URI_RESOLVER = None
""" :py:class:`str`: XSD URI Resolver for lxml validation. Choose from:  None, 'REQUESTS_RESOLVER'.
"""

DISPLAY_EDIT_BUTTON = False
""" boolean: Display the edit button on the result page
"""

DATA_SORTING_FIELDS = ["-last_modification_date"]
""" Array<string>: Default sort fields for the data query. 
"""

DEFAULT_DATE_TOGGLE_VALUE = False
""" boolean: Set the toggle default value in the records list
"""
DATA_DISPLAYED_SORTING_FIELDS = [
    {
        "field": "last_modification_date",
        "display": "Last updated",
        "ordering": "-last_modification_date",
    },
    {
        "field": "last_modification_date",
        "display": "First updated",
        "ordering": "+last_modification_date",
    },
    {"field": "title", "display": "Title (A-Z)", "ordering": "+title"},
    {"field": "title", "display": "Title (Z-A)", "ordering": "-title"},
]
"""The default sorting fields displayed on the GUI, Data model field Array"""
SORTING_DISPLAY_TYPE = "single"
"""Result sorting graphical display type ('multi' / 'single')"""
DISPLAY_PRIVACY_POLICY_FOOTER = True
""" boolean: display the privacy policy link in the footer
"""
DISPLAY_TERMS_OF_USE_FOOTER = True
""" boolean: display the terms of use link in the footer
"""
DISPLAY_CONTACT_FOOTER = True
""" boolean: display the contact link in the footer
"""
DISPLAY_HELP_FOOTER = True
""" boolean: display the help link in the footer
"""
DISPLAY_RULES_OF_BEHAVIOR_FOOTER = True
""" boolean: display the rules of behavior link in the footer
"""

ID_PROVIDER_SYSTEM_NAME = "local"
""" str: internal name of the provider system.
"""

ID_PROVIDER_SYSTEM_CONFIG = {
    "class": "core_linked_records_app.utils.providers.local.LocalIdProvider",
    "args": [],
}
""" dict: provider system configuration for resolving PIDs.
"""

ID_PROVIDER_PREFIXES = (
    os.environ["ID_PROVIDER_PREFIXES"].split(",")
    if "ID_PROVIDER_PREFIXES" in os.environ
    else ["cdcs"]
)
""" list<str>: accepted providers if manually specifying PIDs (first item is the
default prefix)
"""

ID_PROVIDER_PREFIX_DEFAULT = os.getenv(
    "ID_PROVIDER_PREFIX_DEFAULT", ID_PROVIDER_PREFIXES[0]
)

ID_PROVIDER_PREFIX_BLOB = os.getenv(
    "ID_PROVIDER_PREFIX_BLOB", ID_PROVIDER_PREFIXES[0]
)

PID_XPATH = "Resource.@localid"
""" string: location of the PID in the document, specified as dot notation
"""

AUTO_SET_PID = True
""" boolean: enable the automatic pid generation for saved data.
"""

REGISTRY_XSD_FILENAME = "res-md.xsd"
""" str: Registry xsd filename used for the initialisation.
"""

# If you want to use your own schema, set your schema here
REGISTRY_XSD_FILEPATH = os.path.join("xsd", REGISTRY_XSD_FILENAME)
""" str: Registry xsd path used for the initialisation.
"""

# If you want to use your own configuration file, set your configuration file here
CUSTOM_REGISTRY_FILE_PATH = os.path.join("json", "custom_registry.json")
""" str: Custom registry configuration file path used for the initialisation.
"""

# If you want to use your own xslt, set your it here
DEFAULT_DATA_RENDERING_XSLT = os.path.join(
    "core_main_registry_app", "xsl", "xml2html.xsl"
)
""" str: Path to default XSLT to use to render data.
"""

CAN_SET_WORKSPACE_PUBLIC = False
""" boolean: Can private workspace become public
"""

CAN_SET_PUBLIC_DATA_TO_PRIVATE = False
""" boolean: can public data become private
"""

CAN_ANONYMOUS_ACCESS_PUBLIC_DOCUMENT = True
""" boolean: Can anonymous user access public data
"""

ENABLE_XML_ENTITIES_TOOLTIPS = False
""" boolean: enable the xml entities warning tooltip on the GUI.
"""
OAI_ENABLE_HARVESTING = True
""" boolean: Enable OAI-PMH harvesting by default.
"""

ENABLE_SAML2_SSO_AUTH = os.getenv("ENABLE_SAML2_SSO_AUTH", "False").lower() == "true"
""" boolean: enable SAML2 SSO authentication.
"""

ENABLE_HANDLE_PID = os.getenv("ENABLE_HANDLE_PID", "False").lower() == "true"
""" boolean: enable handle server PID support.
"""
