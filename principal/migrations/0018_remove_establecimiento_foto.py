# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0017_auto_20171110_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='establecimiento',
            name='foto',
        ),
    ]
