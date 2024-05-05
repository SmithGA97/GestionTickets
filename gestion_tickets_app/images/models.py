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
    url_cloud = models.URLField(
        verbose_name='url in cloud'
    )
