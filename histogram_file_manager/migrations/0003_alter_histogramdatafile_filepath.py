# Generated by Django 4.0.3 on 2022-03-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histogram_file_manager', '0002_histogramdatafile_data_dimensionality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histogramdatafile',
            name='filepath',
            field=models.FilePathField(help_text='Path where the file is stored', max_length=255, path='/home/mpliax/Desktop/tmp', recursive=True),
        ),
    ]
