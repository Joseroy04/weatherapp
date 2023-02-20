# Generated by Django 4.1.7 on 2023-02-20 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=50, verbose_name='bus name')),
                ('bus_no', models.CharField(max_length=50, unique=True, verbose_name='bus no')),
            ],
            options={
                'verbose_name': 'bus',
                'verbose_name_plural': 'buses',
            },
        ),
        migrations.CreateModel(
            name='bus_stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='city name')),
                ('pincode', models.IntegerField(verbose_name='pincode')),
            ],
            options={
                'verbose_name': 'bus_stop',
                'verbose_name_plural': 'bus_stops',
            },
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=50, verbose_name='driver name')),
                ('license_no', models.CharField(max_length=50, verbose_name='license no')),
                ('age', models.IntegerField(verbose_name='age')),
                ('phone_no', models.IntegerField(verbose_name='phone no')),
            ],
            options={
                'verbose_name': 'driver',
                'verbose_name_plural': 'drivers',
            },
        ),
        migrations.CreateModel(
            name='rutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rute_name', models.CharField(max_length=50, verbose_name='rute name')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bus', verbose_name='bus ')),
                ('bus_driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.driver', verbose_name='deiver ')),
                ('bus_rutes', models.ManyToManyField(to='main.bus_stop', verbose_name=' rutes')),
            ],
            options={
                'verbose_name': 'rutes',
                'verbose_name_plural': 'rutess',
            },
        ),
    ]
