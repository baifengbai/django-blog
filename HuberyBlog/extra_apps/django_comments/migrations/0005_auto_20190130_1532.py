# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-30 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0004_auto_20190130_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replay_name',
            new_name='reply_name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='replay_to',
            new_name='reply_to',
        ),
    ]
