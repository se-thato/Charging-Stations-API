# Generated by Django 5.2.1 on 2025-06-11 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoltHub', '0003_alter_booking_end_time_alter_booking_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chargingpoint',
            old_name='capicity',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='chargingpoint',
            old_name='price_per_hour',
            new_name='off_peak_price',
        ),
        migrations.RemoveField(
            model_name='chargingpoint',
            name='location',
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=255),
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6),
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='charging_speed_kW',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chargingpoint',
            name='peak_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
