# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150719_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dashboarditem',
            name='ext_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='ext_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
