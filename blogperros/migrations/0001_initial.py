# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('imagen', models.FileField(null=True, blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('dpi', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('foto', models.FileField(null=True, blank=True, upload_to='')),
                ('perros', models.ManyToManyField(through='blogperros.Asignacion', to='blogperros.Perro')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='perro',
            field=models.ForeignKey(to='blogperros.Perro'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='persona',
            field=models.ForeignKey(to='blogperros.Persona'),
        ),
    ]
