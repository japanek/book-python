# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kontakt', '0004_auto_20151217_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontakt',
            name='adres',
        ),
        migrations.AddField(
            model_name='adres',
            name='kontakt',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kontakt.Kontakt'),
            preserve_default=False,
        ),
    ]