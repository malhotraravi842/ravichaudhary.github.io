# Generated by Django 3.0.3 on 2020-08-27 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='date',
        ),
        migrations.AddField(
            model_name='job',
            name='endDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='job',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]