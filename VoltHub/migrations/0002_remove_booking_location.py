# Generated by Django 5.2.1 on 2025-06-11 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VoltHub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='location',
        ),
    ]
