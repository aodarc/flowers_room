# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-26 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
