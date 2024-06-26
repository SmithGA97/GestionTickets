# Generated by Django 5.0.4 on 2024-05-04 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField()),
                ('description', models.TextField(blank=True, null=True)),
                ('url_cloud', models.URLField(verbose_name='url in cloud')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='tickets.ticket', verbose_name='ticket')),
            ],
        ),
    ]
