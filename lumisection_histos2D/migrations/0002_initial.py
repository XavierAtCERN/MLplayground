# Generated by Django 4.0.3 on 2022-03-04 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('histogram_file_manager', '0001_initial'),
        ('lumisection_histos2D', '0001_initial'),
        ('lumisections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lumisectionhisto2d',
            name='lumisection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lumisections.lumisection'),
        ),
        migrations.AddField(
            model_name='lumisectionhisto2d',
            name='source_data_file',
            field=models.ForeignKey(blank=True, help_text='Source data file that the specific Histogram was read from, if any', null=True, on_delete=django.db.models.deletion.SET_NULL, to='histogram_file_manager.histogramdatafile'),
        ),
        migrations.AddConstraint(
            model_name='lumisectionhisto2d',
            constraint=models.UniqueConstraint(fields=('lumisection', 'title'), name='unique run / ls / 2d histogram combination'),
        ),
    ]
