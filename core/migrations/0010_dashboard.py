# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161006_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(max_length=4, verbose_name='Ano')),
                ('mes', models.IntegerField(max_length=2, verbose_name='Mês')),
                ('rendimentos', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Rendimentos')),
                ('despesas', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Despesas')),
                ('media_gastos', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Média de gasto diário')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Saldo')),
                ('saldo_acumulado', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Saldo acumulado')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update time')),
            ],
        ),
    ]