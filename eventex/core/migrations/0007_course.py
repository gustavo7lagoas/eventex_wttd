# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-02 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180223_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='Início')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='Palestrantes')),
            ],
            options={
                'verbose_name': 'Palestra',
                'verbose_name_plural': 'Palestras',
                'abstract': False,
            },
        ),
    ]
