from django.db import models
from tickets.models import Ticket

# Create your models here.
class Image(models.Model):
    ticket_id = models.ForeignKey(
        Ticket, on_delete=models.CASCADE,
        null = False,
        blank = False,
        related_name='ticket',
        verbose_name='ticket'
    )
    tittle = models.CharField(
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    cloud_info = models.TextField(
        verbose_name='Metadata in Cloud',
        null=True,
        blank=True
    )
