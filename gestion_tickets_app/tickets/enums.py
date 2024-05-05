# Core Django imports
from django.db import models

class Status(models.TextChoices):
    NOT_STARTED = 'NOT_STARTED', 'Not started'
    IN_PROCESS = 'IN_PROCESS', 'In process'
    COMPLETED = 'COMPLETED', 'Completed'