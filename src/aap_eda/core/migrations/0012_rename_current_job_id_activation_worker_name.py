# Generated by Django 3.2.18 on 2023-09-18 18:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_auto_20230922_1431"),
    ]

    operations = [
        migrations.RenameField(
            model_name="activation",
            old_name="current_job_id",
            new_name="worker_name",
        ),
    ]