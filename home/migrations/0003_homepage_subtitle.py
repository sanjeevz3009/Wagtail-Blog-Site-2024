# Generated by Django 5.0.9 on 2024-10-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="subtitle",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]