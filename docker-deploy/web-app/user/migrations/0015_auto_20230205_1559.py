# Generated by Django 3.2.16 on 2023-02-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20230205_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_shared',
            field=models.BooleanField(choices=[('False', 'False'), ('True', 'True')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unknown', 'unknown')], default='unknown', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('SUV', 'SUV'), ('Sedan', 'Sedan')], default='Sedan', max_length=256),
        ),
    ]