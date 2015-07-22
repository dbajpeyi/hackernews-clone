# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150720_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboarditem',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='dashboarditem',
            unique_together=set([('profile', 'item')]),
        ),
    ]
