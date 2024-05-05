# Generated by Django 5.0.4 on 2024-05-04 21:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField()),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('number_of_images', models.IntegerField(verbose_name='number of images')),
                ('uploaded_images', models.IntegerField(verbose_name='number of uploaded images')),
                ('status', models.CharField(choices=[('NOT_STARTED', 'Not started'), ('IN_PROCESS', 'In process'), ('COMPLETED', 'Completed')], default='NOT_STARTED')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='created by')),
            ],
        ),
    ]
