# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170909_0339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationprofile',
            options={'verbose_name': 'Organization profile', 'verbose_name_plural': 'Organization profiles'},
        ),
    ]
