# Generated by Django 3.2.16 on 2023-02-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20230205_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('unknown', 'unknown'), ('female', 'female'), ('male', 'male')], default='unknown', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('SUV', 'SUV'), ('Sports Car', 'Sports Car'), ('Sedan', 'Sedan')], default='Sedan', max_length=64),
        ),
    ]
