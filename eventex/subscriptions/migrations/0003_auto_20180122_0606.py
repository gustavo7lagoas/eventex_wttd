# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20180119_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
