# Generated by Django 4.0.3 on 2022-03-04 17:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LumisectionHisto2D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, size=None)),
                ('entries', models.IntegerField(blank=True, null=True)),
                ('x_min', models.FloatField(blank=True, null=True)),
                ('x_max', models.FloatField(blank=True, null=True)),
                ('x_bin', models.IntegerField(blank=True, null=True)),
                ('y_max', models.FloatField(blank=True, null=True)),
                ('y_min', models.FloatField(blank=True, null=True)),
                ('y_bin', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
