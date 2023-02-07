# Generated by Django 4.1.6 on 2023-02-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_user_sex'),
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
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('SUV', 'SUV'), ('Sedan', 'Sedan')], default='Sedan', max_length=64),
        ),
    ]
