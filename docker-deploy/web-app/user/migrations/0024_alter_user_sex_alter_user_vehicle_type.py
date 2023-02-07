# Generated by Django 4.1.5 on 2023-02-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_user_sex_alter_user_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male'), ('unknown', 'unknown')], default='unknown', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('SUV', 'SUV'), ('Sports Car', 'Sports Car'), ('Sedan', 'Sedan')], default='Sedan', max_length=64),
        ),
    ]
