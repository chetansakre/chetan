# Generated by Django 4.2.3 on 2023-08-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_employee_gender_alter_employee_marital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='FY',
            fields=[
                ('financial_year', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('set_current', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='HolidayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_year', models.CharField(choices=[('2023-2024', '2023-2024'), ('2022-2023', '2022-2023')], max_length=10)),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_type', models.CharField(choices=[('fixed', 'fixed'), ('optional', 'optional')], max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
