# Generated by Django 3.2.16 on 2023-02-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20230205_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('Sedan', 'Sedan'), ('SUV', 'SUV')], default='Sedan', max_length=256),
        ),
    ]
