# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-23 21:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemoverview',
            name='installed_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 21, 25, 52, 393363)),
        ),
        migrations.AlterField(
            model_name='systemoverview',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 23, 21, 25, 52, 393301)),
        ),
    ]
