# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-08 13:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='DeviceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.TextField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Device')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('sex', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'T', b'Other')], default=b'M', max_length=1)),
                ('age', models.FloatField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ResidentActions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Resident')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ResidentActionTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ResidentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfactory', models.BooleanField()),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Resident')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ResidentState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.FloatField()),
                ('height', models.FloatField()),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Room')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='SensorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='SensorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('value', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Sensor')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.SensorType'),
        ),
        migrations.AddField(
            model_name='residentresponse',
            name='sensor_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.SensorValue'),
        ),
        migrations.AddField(
            model_name='residentactiontypes',
            name='result_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ResidentState'),
        ),
        migrations.AddField(
            model_name='residentactions',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ResidentActionTypes'),
        ),
        migrations.AddField(
            model_name='resident',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ResidentState'),
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Room'),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.DeviceType'),
        ),
    ]
