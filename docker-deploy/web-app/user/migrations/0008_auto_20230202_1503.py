# Generated by Django 3.2.16 on 2023-02-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20230201_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_comfirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('open', 'open')], default='open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('unknown', 'unknown'), ('female', 'female')], default='unknown', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Sports Car', 'Sports Car'), ('SUV', 'SUV')], default='Sedan', max_length=256),
        ),
    ]
