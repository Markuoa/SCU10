# Generated by Django 4.1.3 on 2022-11-26 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("secondhand_book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="goods",
            name="Commodity_Name",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
