# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0020_auto_20170810_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='featured',
        ),
        migrations.AddField(
            model_name='client',
            name='priority',
            field=models.IntegerField(default=False, help_text='The order in which to display. A high number means high priority', verbose_name='priority'),
        ),
    ]