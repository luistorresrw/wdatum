# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_auto_20171207_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='agroquimico',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='agroquimicousado',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='encuestado',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='familia',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='invernaculo',
            name='transaccion',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='agroquimico',
            name='asesoramientoOtro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]