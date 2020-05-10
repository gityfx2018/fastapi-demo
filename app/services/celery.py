from __future__ import absolute_import
from celery import Celery

from ..db import celeryconfig

celery_app = Celery(
    "worker",
)

celery_app.config_from_object(celeryconfig)