# Generated by Django 5.0.2 on 2024-03-23 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_dailyreport_report_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='report_text',
        ),
        migrations.AddField(
            model_name='dailyreport',
            name='report_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='dailyreport',
            name='report_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]