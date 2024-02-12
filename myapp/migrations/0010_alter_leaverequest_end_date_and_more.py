# Generated by Django 4.2.3 on 2023-08-27 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_employee_leave_balance_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='end_date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='start_date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
        migrations.DeleteModel(
            name='Leave',
        ),
    ]
