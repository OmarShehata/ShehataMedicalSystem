# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0002_auto_20150625_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='hospital',
            field=models.ForeignKey(to='medical.Hospital'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(to='medical.Patient'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='referral',
            field=models.ForeignKey(to='medical.Referrer'),
        ),
    ]
