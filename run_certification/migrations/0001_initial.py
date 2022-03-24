# Generated by Django 4.0.3 on 2022-03-24 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_taking_objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rr_is_pixel_good', models.BooleanField(null=True)),
                ('rr_is_strip_good', models.BooleanField(null=True)),
                ('rr_is_ecal_good', models.BooleanField(null=True)),
                ('rr_is_hcal_good', models.BooleanField(null=True)),
                ('rr_is_dt_good', models.BooleanField(null=True)),
                ('rr_is_csc_good', models.BooleanField(null=True)),
                ('rr_is_tracking_good', models.BooleanField(null=True)),
                ('rr_is_muon_good', models.BooleanField(null=True)),
                ('rr_is_egamma_good', models.BooleanField(null=True)),
                ('rr_is_tau_good', models.BooleanField(null=True)),
                ('rr_is_jetmet_good', models.BooleanField(null=True)),
                ('rr_is_btag_good', models.BooleanField(null=True)),
                ('rr_frac_pixel_good', models.FloatField(null=True)),
                ('rr_frac_strip_good', models.FloatField(null=True)),
                ('rr_frac_ecal_good', models.FloatField(null=True)),
                ('rr_frac_hcal_good', models.FloatField(null=True)),
                ('rr_frac_dt_good', models.FloatField(null=True)),
                ('rr_frac_csc_good', models.FloatField(null=True)),
                ('rr_frac_tracking_good', models.FloatField(null=True)),
                ('rr_frac_muon_good', models.FloatField(null=True)),
                ('rr_frac_egamma_good', models.FloatField(null=True)),
                ('rr_frac_tau_good', models.FloatField(null=True)),
                ('rr_frac_jetmet_good', models.FloatField(null=True)),
                ('rr_frac_btag_good', models.FloatField(null=True)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_taking_objects.run')),
            ],
        ),
    ]
