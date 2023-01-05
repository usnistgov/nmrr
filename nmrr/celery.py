""" Celery instance configuration
"""
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nmrr.settings")

from django.conf import settings  # noqa

app = Celery("nmrr")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings")

# Autodiscover tasks : tasks.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
