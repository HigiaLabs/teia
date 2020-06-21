import os
from celery import Celery
from django.conf import settings
from prettyconf import Configuration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")

app = Celery('enriquecimento-dados')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
