# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_entry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]