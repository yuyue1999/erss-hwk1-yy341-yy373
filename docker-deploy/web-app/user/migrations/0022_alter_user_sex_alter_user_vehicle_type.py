# Generated by Django 4.1.5 on 2023-02-06 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20230205_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('female', 'female'), ('unknown', 'unknown'), ('male', 'male')], default='unknown', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Sports Car', 'Sports Car')], default='Sedan', max_length=64),
        ),
    ]
