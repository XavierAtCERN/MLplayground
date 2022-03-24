# Generated by Django 4.0.3 on 2022-03-24 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_number', models.IntegerField(unique=True)),
                ('run_date', models.DateTimeField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('period', models.CharField(blank=True, max_length=1, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('oms_fill', models.IntegerField(blank=True, null=True)),
                ('oms_lumisections', models.IntegerField(blank=True, null=True)),
                ('oms_initial_lumi', models.FloatField(blank=True, null=True)),
                ('oms_end_lumi', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lumisection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ls_number', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('oms_zerobias_rate', models.FloatField(blank=True, null=True)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_taking_objects.run')),
            ],
        ),
        migrations.AddConstraint(
            model_name='lumisection',
            constraint=models.UniqueConstraint(fields=('run', 'ls_number'), name='unique run/ls combination'),
        ),
    ]
