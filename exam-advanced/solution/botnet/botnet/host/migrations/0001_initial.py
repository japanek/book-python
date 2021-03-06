# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 14:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Datetime')),
                ('host', models.GenericIPAddressField(db_index=True, verbose_name='Host')),
                ('port', models.PositiveIntegerField(help_text='1025-65535', validators=[django.core.validators.MinValueValidator(1025), django.core.validators.MaxValueValidator(65535)], verbose_name='Port')),
            ],
            options={
                'verbose_name': 'Host',
                'verbose_name_plural': 'Hosts',
            },
        ),
    ]
