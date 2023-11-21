# Generated by Django 4.1.13 on 2023-11-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("Review_ID", models.CharField(max_length=10)),
                ("Rating", models.IntegerField()),
                ("Text", models.CharField(max_length=1000)),
                ("Branch", models.CharField(max_length=255)),
            ],
        ),
    ]
