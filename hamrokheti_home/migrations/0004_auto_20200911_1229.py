# Generated by Django 3.1 on 2020-09-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamrokheti_home', '0003_fundfarm_roi_in_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundfarm',
            name='roi_in_percent',
            field=models.CharField(max_length=3),
        ),
    ]
