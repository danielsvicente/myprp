# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160927_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='transaction_type',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='core.TransactionType'),
        ),
    ]
