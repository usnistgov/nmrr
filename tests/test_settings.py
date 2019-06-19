SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    # Extra apps
    "password_policies",

    # Local apps
    "core_main_app",
    "core_main_app.tests",

]
