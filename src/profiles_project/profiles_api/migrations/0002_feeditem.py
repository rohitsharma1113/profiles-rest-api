# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 17:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status_text', models.CharField(max_length=255)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
