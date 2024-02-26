# Generated by Django 4.1.3 on 2024-02-15 11:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0005_battlejob"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=25, verbose_name="Character Name"),
                ),
                ("appartment_location", models.CharField(max_length=30)),
                ("estate_location", models.CharField(max_length=30)),
                (
                    "home_world",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="core.world"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Characters",
            },
        ),
    ]
