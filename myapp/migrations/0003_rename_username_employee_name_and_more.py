# Generated by Django 4.2.3 on 2023-08-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_email_employee_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='LeaveRequest',
        ),
        migrations.DeleteModel(
            name='LeaveType',
        ),
    ]
