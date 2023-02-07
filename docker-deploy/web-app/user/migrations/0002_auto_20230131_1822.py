# Generated by Django 3.2.16 on 2023-01-31 23:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='Username')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=32)),
                ('is_driver', models.BooleanField(blank=True, default=False, null=True)),
                ('full_name', models.CharField(blank=True, max_length=128, null=True)),
                ('vehicle_type', models.CharField(blank=True, max_length=256, null=True)),
                ('plate_num', models.CharField(blank=True, max_length=256, null=True)),
                ('max_passenger', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('special_vehicle_info', models.CharField(blank=True, max_length=256, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
