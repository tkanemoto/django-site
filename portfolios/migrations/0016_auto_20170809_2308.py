# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0015_auto_20170809_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='', max_length=30, verbose_name='category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.CharField(default='', max_length=20, verbose_name='date'),
            preserve_default=False,
        ),
    ]
