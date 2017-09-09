# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20170909_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='category',
        ),
        migrations.AddField(
            model_name='organization',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='organizations', to='organization.Category'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='external_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID in KRS database'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='flat_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='krs',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='nip',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='purpose',
            field=models.TextField(blank=True, verbose_name='Purpose of the organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='register_at',
            field=models.DateField(blank=True, null=True, verbose_name='Date of the registration'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='short_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Short name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organization',
            name='street_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
