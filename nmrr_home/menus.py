""" Menu configuration for nmrr.

  * Help menu

    * API Documentation
    * Contact
    * Help
"""

from django.urls import reverse
from menu import Menu, MenuItem

Menu.add_item(
    "help", MenuItem("API Documentation", reverse("swagger_view"), icon="cogs")
)

Menu.add_item(
    "help",
    MenuItem("Contact", reverse("core_website_app_contact"), icon="envelope"),
)

Menu.add_item(
    "help",
    MenuItem("Help", reverse("core_website_app_help"), icon="question-circle"),
)
