# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('url', models.URLField(max_length=400)),
                ('hacker_news_url', models.URLField()),
                ('points', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='dashboarditem',
            name='item',
            field=models.ForeignKey(to='news.NewsItem'),
        ),
        migrations.AddField(
            model_name='dashboarditem',
            name='profile',
            field=models.ForeignKey(to='news.UserProfile'),
        ),
    ]
