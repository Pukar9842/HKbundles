# Generated by Django 3.1 on 2020-09-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrokheti_home', '0007_auto_20200913_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundfarm',
            name='tenure_for_ROI',
            field=models.IntegerField(max_length=10),
        ),
    ]
