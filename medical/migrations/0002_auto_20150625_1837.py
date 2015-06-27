# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='state',
            field=models.CharField(default='new', max_length=50),
        ),
        migrations.AlterField(
            model_name='visit',
            name='lastSeen',
            field=models.DateField(auto_now=True),
        ),
    ]
