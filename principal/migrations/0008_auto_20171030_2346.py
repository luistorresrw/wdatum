# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20171030_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establecimiento',
            name='foto',
            field=models.ImageField(null=True, upload_to='principal/static/img/establecimientos/'),
        ),
    ]
