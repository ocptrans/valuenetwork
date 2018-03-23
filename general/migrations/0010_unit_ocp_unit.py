# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valueaccounting', '0013_auto_20171106_1539'),
        ('general', '0009_auto_20170907_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='ocp_unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='valueaccounting.Unit', verbose_name='OCP Unit'),
        ),
    ]