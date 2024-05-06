from django.db import models
from django.contrib.auth.models import User
from .enums import Status

# Create your models here.

class Ticket(models.Model):
    tittle = models.CharField(
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creation date',
        editable=False
    )
    number_of_images = models.IntegerField(
        verbose_name='number of images'
    )
    uploaded_images = models.IntegerField(
        verbose_name = 'number of uploaded images',
        default=0
    )
    status = models.CharField(
        choices=Status.choices,
        default = Status.NOT_STARTED
    )
    created_by = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        null = False,
        blank = False,
        editable = False,
        related_name = 'user',
        to_field = 'username',
        verbose_name='created by'
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    def increment_images_count(self):
        self.uploaded_images += 1
        self.save()

    def __str__(self) -> str:
        return f'{self.tittle} by {self.created_by}'
