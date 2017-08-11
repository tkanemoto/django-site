# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0012_auto_20170809_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='page',
        ),
        migrations.AddField(
            model_name='page',
            name='clients',
            field=models.ManyToManyField(blank=True, to='portfolios.Client'),
        ),
    ]