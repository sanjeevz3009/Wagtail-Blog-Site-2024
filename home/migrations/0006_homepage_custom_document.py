# Generated by Django 5.0.9 on 2024-11-10 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0001_initial"),
        ("home", "0005_homepage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="custom_document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="documents.customdocument",
            ),
        ),
    ]
