# Generated by Django 3.1 on 2020-09-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrokheti_home', '0005_fundfarm_tenure_for_roi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundfarm',
            name='tenure_for_ROI',
            field=models.CharField(max_length=10),
        ),
    ]