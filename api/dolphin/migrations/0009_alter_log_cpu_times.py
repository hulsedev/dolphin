# Generated by Django 4.0.6 on 2022-07-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolphin', '0008_alter_log_cpu_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='cpu_times',
            field=models.JSONField(),
        ),
    ]
