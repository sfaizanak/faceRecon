# Generated by Django 5.0.3 on 2024-03-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("faceRecon", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmodel",
            name="img_encoded",
            field=models.BinaryField(null=True),
        ),
    ]