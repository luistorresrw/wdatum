# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-08 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_auto_20171108_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('1', 'Administrador'), ('2', 'Operador'), ('3', 'Encuestador')], default='SOME STRING', max_length=15),
        ),
    ]
