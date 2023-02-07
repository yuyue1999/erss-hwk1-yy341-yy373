# Generated by Django 4.1.6 on 2023-02-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_alter_user_sex_alter_user_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Sports Car', 'Sports Car'), ('SUV', 'SUV')], default='Sedan', max_length=64),
        ),
    ]
