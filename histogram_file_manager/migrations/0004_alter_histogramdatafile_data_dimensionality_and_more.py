# Generated by Django 4.0.4 on 2022-04-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histogram_file_manager', '0003_alter_histogramdatafile_data_dimensionality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histogramdatafile',
            name='data_dimensionality',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'Unknown'), (1, '1D'), (2, '2D')], default=0),
        ),
        migrations.AlterField(
            model_name='histogramdatafile',
            name='granularity',
            field=models.CharField(choices=[('unk', 'Unknown'), ('run', 'Run'), ('lum', 'Lumisection')], default='unk', help_text='The granularity of the data contained in the data file (either whole run or lumisections)', max_length=3),
        ),
    ]
