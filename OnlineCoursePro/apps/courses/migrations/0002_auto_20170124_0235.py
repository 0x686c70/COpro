# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-24 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('easy', '\u521d\u7ea7'), ('middle', '\u4e2d\u7ea7'), ('hard', '\u9ad8\u7ea7')], max_length=20, verbose_name='\u96be\u5ea6'),
        ),
    ]
