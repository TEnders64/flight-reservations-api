# Generated by Django 4.2.13 on 2024-06-07 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_alter_reservation_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.passenger'),
        ),
    ]
