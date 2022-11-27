# Generated by Django 4.1.3 on 2022-11-26 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                ("UserID", models.AutoField(primary_key=True, serialize=False)),
                ("Username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("Email", models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Goods",
            fields=[
                ("Commodity_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Price", models.IntegerField()),
                ("Contact_QQ", models.DecimalField(decimal_places=0, max_digits=11)),
                ("Note", models.CharField(max_length=120)),
                ("Date", models.DateTimeField(auto_now_add=True)),
                (
                    "UserID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="UserID_Goods",
                        to="secondhand_book.userinfo",
                    ),
                ),
            ],
        ),
    ]
