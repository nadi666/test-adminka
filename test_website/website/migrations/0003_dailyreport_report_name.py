# Generated by Django 5.0.2 on 2024-03-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_manager_remove_dailyreport_manager_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='report_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
