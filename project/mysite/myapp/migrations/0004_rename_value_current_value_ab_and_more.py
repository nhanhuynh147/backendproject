# Generated by Django 4.2.3 on 2023-12-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_power_voltage_rename_feature_current'),
    ]

    operations = [
        migrations.RenameField(
            model_name='current',
            old_name='Value',
            new_name='Value_AB',
        ),
        migrations.RenameField(
            model_name='voltage',
            old_name='Value',
            new_name='Value_AB',
        ),
        migrations.AddField(
            model_name='current',
            name='Value_AN',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='current',
            name='Value_BC',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='current',
            name='Value_BN',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='current',
            name='Value_CA',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='current',
            name='Value_CN',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='voltage',
            name='Value_AN',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='voltage',
            name='Value_BC',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='voltage',
            name='Value_BN',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='voltage',
            name='Value_CA',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='voltage',
            name='Value_CN',
            field=models.FloatField(default=0),
        ),
    ]
