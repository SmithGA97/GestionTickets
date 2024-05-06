import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion_tickets_app.settings")
app = Celery("gestion_tickets_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
