# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_auto_20170825_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='comicseries',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
