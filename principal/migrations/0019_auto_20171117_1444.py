# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_remove_establecimiento_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agroquimico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usa', models.BooleanField(default=False)),
                ('asesoramientoOtro', models.CharField(max_length=50)),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'agroquimico',
            },
        ),
        migrations.CreateModel(
            name='AgroquimicoUsado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('plaga', models.CharField(max_length=50)),
                ('metodo_aplicacion', models.CharField(max_length=50)),
                ('frecuencia_uso', models.CharField(max_length=50)),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'agroquimico_usado',
            },
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroSiembra', models.IntegerField()),
                ('mesSiembra', models.IntegerField()),
                ('surcos', models.IntegerField()),
                ('distancias', models.IntegerField()),
                ('largo', models.IntegerField()),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'cultivo',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
                ('agroquimico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Agroquimico')),
            ],
            options={
                'db_table': 'encuesta',
            },
        ),
        migrations.CreateModel(
            name='Encuestado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('nivelCompleto', models.BooleanField(default=False)),
                ('viveEstablecimiento', models.BooleanField(default=False)),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'encuestado',
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esCasado', models.BooleanField()),
                ('tieneHijos', models.BooleanField()),
                ('cantVarones', models.IntegerField()),
                ('cantMujeres', models.IntegerField()),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'familia',
            },
        ),
        migrations.CreateModel(
            name='Invernaculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadModulos', models.IntegerField()),
                ('superficieUnitaria', models.IntegerField()),
                ('creado', models.DateField(default=None)),
                ('modificado', models.DateField(default=None)),
                ('eliminado', models.DateField(default=None)),
            ],
            options={
                'db_table': 'invernaculo',
            },
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='creado',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='eliminado',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos/'),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='modificado',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='regimenOtros',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='regimenTenencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.RegimenTenencia'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='anioconstruccion',
            table='anio_construccion',
        ),
        migrations.AlterModelTable(
            name='asesoramiento',
            table='asesoramiento',
        ),
        migrations.AlterModelTable(
            name='eleccioncultivo',
            table='eleccion_cultivo',
        ),
        migrations.AlterModelTable(
            name='especie',
            table='especie',
        ),
        migrations.AlterModelTable(
            name='establecimiento',
            table='establecimiento',
        ),
        migrations.AlterModelTable(
            name='factorclimatico',
            table='factor_climatico',
        ),
        migrations.AlterModelTable(
            name='materialestructura',
            table='material_construccion',
        ),
        migrations.AlterModelTable(
            name='nacionalidad',
            table='nacionalidad',
        ),
        migrations.AlterModelTable(
            name='nivelinstruccion',
            table='nivel_instrucion',
        ),
        migrations.AlterModelTable(
            name='regimentenencia',
            table='regimen_tenencia',
        ),
        migrations.AlterModelTable(
            name='tipocultivo',
            table='tipo_cultivo',
        ),
        migrations.AlterModelTable(
            name='tipoproduccion',
            table='tipo_produccion',
        ),
        migrations.AlterModelTable(
            name='triplelavado',
            table='triple_lavado',
        ),
        migrations.AddField(
            model_name='invernaculo',
            name='anioContruccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.AnioConstruccion'),
        ),
        migrations.AddField(
            model_name='invernaculo',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Encuesta'),
        ),
        migrations.AddField(
            model_name='invernaculo',
            name='materialEstructura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.MaterialEstructura'),
        ),
        migrations.AddField(
            model_name='encuestado',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Nacionalidad'),
        ),
        migrations.AddField(
            model_name='encuestado',
            name='nivelInstruccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.NivelInstruccion'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='encuestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Encuestado'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='establecimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Establecimiento'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Familia'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='eleccionCultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.EleccionCultivo'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Encuesta'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Especie'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.TipoCultivo'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='tipoProducion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.TipoProduccion'),
        ),
        migrations.AddField(
            model_name='agroquimicousado',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Encuesta'),
        ),
        migrations.AddField(
            model_name='agroquimico',
            name='asesoramiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Asesoramiento'),
        ),
        migrations.AddField(
            model_name='agroquimico',
            name='factorClimatico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.FactorClimatico'),
        ),
        migrations.AddField(
            model_name='agroquimico',
            name='tripleLavado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.TripleLavado'),
        ),
    ]
