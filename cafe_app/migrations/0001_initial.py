# Generated by Django 4.1.2 on 2023-01-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cafe",
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
                ("nama_cafe", models.CharField(max_length=50)),
                ("alamat", models.TextField(null=True)),
                ("no_tlp", models.CharField(max_length=20)),
                ("koordinat", models.CharField(max_length=50)),
                ("img", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
