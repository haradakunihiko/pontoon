# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_auto_20160713_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='from_django_browserid',
            field=models.BooleanField(default=False),
        ),
    ]
