# Generated by Django 4.2.3 on 2023-08-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_leaverequest_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
