# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='nip',
            field=models.CharField(max_length=255),
        ),
    ]
