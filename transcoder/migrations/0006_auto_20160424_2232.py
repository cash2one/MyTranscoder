# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcoder', '0005_auto_20160424_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcodertask',
            name='endtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='transcodertask',
            name='satrttime',
            field=models.DateTimeField(null=True),
        ),
    ]
