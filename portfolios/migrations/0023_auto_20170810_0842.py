# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0022_auto_20170810_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='background',
            field=models.ImageField(blank=True, help_text='Background image to display in the carousel', null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='client',
            name='mugshot',
            field=models.ImageField(blank=True, help_text='Profile picture', null=True, upload_to=b''),
        ),
    ]