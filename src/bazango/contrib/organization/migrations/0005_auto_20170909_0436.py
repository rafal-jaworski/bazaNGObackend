# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170909_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='organizationprofile',
            name='www',
            field=models.URLField(blank=True),
        ),
    ]
