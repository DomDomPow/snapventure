# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapventure', '0023_step_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='order_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
