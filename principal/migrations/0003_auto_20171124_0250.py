# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20171124_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='agroquimico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Agroquimico'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='creado',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='eliminado',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Familia'),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='modificado',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]