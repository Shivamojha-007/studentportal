# Generated by Django 4.1 on 2022-08-19 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notes",
            options={"verbose_name": "notes", "verbose_name_plural": "notes"},
        ),
    ]
