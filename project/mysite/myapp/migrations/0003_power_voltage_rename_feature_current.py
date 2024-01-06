# Generated by Django 4.2.3 on 2023-12-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_feature_detail_feature_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voltage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Value', models.FloatField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Feature',
            new_name='Current',
        ),
    ]