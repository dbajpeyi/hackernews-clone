# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150720_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hacker_news_url',
            field=models.URLField(unique=True),
        ),
    ]
