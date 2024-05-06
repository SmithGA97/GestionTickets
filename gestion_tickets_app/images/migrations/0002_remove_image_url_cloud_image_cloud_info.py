# Generated by Django 5.0.4 on 2024-05-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url_cloud',
        ),
        migrations.AddField(
            model_name='image',
            name='cloud_info',
            field=models.TextField(blank=True, null=True, verbose_name='Metadata in Cloud'),
        ),
    ]