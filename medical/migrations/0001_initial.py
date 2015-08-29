# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('sectionData', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dateofbirth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('firstvisit', models.DateField(auto_now_add=True)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('refType', models.CharField(max_length=50)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('state', models.CharField(default='new', max_length=50)),
                ('hospitalID', models.CharField(default=-1, max_length=50)),
                ('billingPaid', models.FloatField(default=0)),
                ('billingTotal', models.FloatField(default=1)),
                ('diagnosis_report', models.TextField(blank=True)),
                ('treatment_report', models.TextField(blank=True)),
                ('followup_report', models.TextField(blank=True)),
                ('lastSeen', models.DateField(auto_now=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('meta', models.TextField(blank=True)),
                ('diagnosis', models.ForeignKey(to='medical.Diagnosis_Category', related_name='diagnosis_category')),
                ('followup', models.ForeignKey(to='medical.Diagnosis_Category', related_name='followup_category')),
                ('hospital', models.ForeignKey(to='medical.Hospital', null=True)),
                ('patient', models.ForeignKey(to='medical.Patient')),
                ('referral', models.ForeignKey(to='medical.Referrer', null=True)),
                ('treatment', models.ForeignKey(to='medical.Diagnosis_Category', related_name='treatment_category')),
            ],
        ),
    ]
