# Generated by Django 5.0.4 on 2024-05-04 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uploaded_images',
            field=models.IntegerField(default=0, verbose_name='number of uploaded images'),
        ),
    ]