# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='diagnosis',
            field=models.ForeignKey(to='medical.Diagnosis_Category', null=True, related_name='diagnosis_category'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='followup',
            field=models.ForeignKey(to='medical.Diagnosis_Category', null=True, related_name='followup_category'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='treatment',
            field=models.ForeignKey(to='medical.Diagnosis_Category', null=True, related_name='treatment_category'),
        ),
    ]
