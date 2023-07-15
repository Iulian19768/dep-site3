# Generated by Django 4.1.5 on 2023-07-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("nume", models.CharField(max_length=100)),
                ("numar_tel", models.IntegerField()),
                ("email", models.CharField(max_length=100)),
                ("date", models.CharField(max_length=100)),
                ("time", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
            ],
        ),
    ]
