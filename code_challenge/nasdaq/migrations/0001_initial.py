# Generated by Django 4.1.1 on 2022-09-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MostTraded",
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
                ("index", models.IntegerField(blank=True, null=True)),
                ("symbol", models.TextField(blank=True, null=True)),
                ("volume", models.FloatField(blank=True, null=True)),
            ],
            options={"db_table": "most_traded", "managed": False,},
        ),
    ]
