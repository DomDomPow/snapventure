# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snapventure', '0019_auto_20161221_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
