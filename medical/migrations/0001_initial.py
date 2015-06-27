# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('dateofbirth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=50)),
                ('firstvisit', models.DateField(auto_now_add=True)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='referrer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('refType', models.CharField(max_length=50)),
                ('meta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('hospitalID', models.CharField(max_length=50)),
                ('billingPaid', models.FloatField()),
                ('billingTotal', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('diagnosis', models.TextField(blank=True)),
                ('followupCategory', models.CharField(max_length=50)),
                ('followupInfo', models.TextField(blank=True)),
                ('lastSeen', models.DateField(auto_now_add=True)),
                ('meta', models.TextField(blank=True)),
                ('hospital', models.ForeignKey(to='medical.hospital')),
                ('patient', models.ForeignKey(to='medical.patient')),
                ('referral', models.ForeignKey(to='medical.referrer')),
            ],
        ),
    ]
