# Generated by Django 4.1.4 on 2023-01-19 18:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spending',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='botAPI.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='referralcode',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 18, 42, 56, 470083)),
        ),
    ]
