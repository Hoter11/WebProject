# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('hide', models.BooleanField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
