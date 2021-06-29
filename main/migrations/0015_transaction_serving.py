# Generated by Django 3.2.3 on 2021-06-29 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_auto_20210622_1452"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="serving",
            field=models.DecimalField(
                decimal_places=2,
                default=1,
                max_digits=19,
                verbose_name="Размер порции (0,5, 1, 2)",
            ),
        ),
    ]
