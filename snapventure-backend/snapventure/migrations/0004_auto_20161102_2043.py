# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapventure', '0003_auto_20161102_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='content_url',
            field=models.URLField(blank=True),
        ),
    ]