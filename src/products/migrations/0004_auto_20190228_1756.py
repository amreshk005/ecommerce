# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-28 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190227_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
