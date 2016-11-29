# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160927_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of transaction')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('document', models.CharField(max_length=10, verbose_name='Document')),
                ('value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Value')),
            ],
        ),
        migrations.RenameModel(
            old_name='MovimentType',
            new_name='TransactionType',
        ),
        migrations.RemoveField(
            model_name='moviment',
            name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='moviment_type',
            new_name='transaction_type',
        ),
        migrations.DeleteModel(
            name='Moviment',
        ),
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category'),
        ),
    ]
