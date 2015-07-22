# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150719_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.UUIDField(default=uuid.uuid4, unique=True, editable=False)),
                ('url', models.URLField(max_length=400)),
                ('hacker_news_url', models.URLField()),
                ('points', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('posted_on', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='dashboarditem',
            old_name='read',
            new_name='is_read',
        ),
        migrations.AlterField(
            model_name='dashboarditem',
            name='item',
            field=models.ForeignKey(to='news.Item'),
        ),
        migrations.DeleteModel(
            name='NewsItem',
        ),
    ]
