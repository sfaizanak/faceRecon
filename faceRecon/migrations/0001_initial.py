# Generated by Django 5.0.3 on 2024-03-20 17:33

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="collegeAdmin",
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
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("collegeName", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="studentModel",
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
                ("studentName", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("collegeName", models.CharField(max_length=100)),
                ("dept", models.CharField(max_length=50)),
                ("year", models.CharField(max_length=10)),
                ("mobile", models.BigIntegerField()),
                ("addr", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=20)),
                (
                    "name_slug",
                    autoslug.fields.AutoSlugField(
                        default=None,
                        editable=False,
                        null=True,
                        populate_from="studentName",
                        unique=True,
                    ),
                ),
                ("img", models.FileField(upload_to="studentImg/")),
                ("img_encoded", models.BigIntegerField(null=True)),
            ],
        ),
    ]
