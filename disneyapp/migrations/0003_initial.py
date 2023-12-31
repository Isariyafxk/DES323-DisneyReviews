# Generated by Django 4.1.13 on 2023-11-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("disneyapp", "0002_delete_disneylandreview"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisneylandReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review_id", models.CharField(max_length=10000)),
                ("rating", models.IntegerField()),
                ("text", models.CharField(max_length=1000)),
                ("branch", models.CharField(max_length=255)),
            ],
        ),
    ]
