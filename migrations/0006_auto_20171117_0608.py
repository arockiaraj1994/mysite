# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20171117_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mysite.Role'),
        ),
    ]