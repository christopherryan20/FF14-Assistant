# Generated by Django 4.1.3 on 2024-02-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("character", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="appartment_location",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="character",
            name="estate_location",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
