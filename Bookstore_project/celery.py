import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bookstore_project.settings')
app = Celery('Bookstore_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()