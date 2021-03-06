# Generated by Django 3.2.3 on 2021-06-13 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_accountant",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="Это бухгалтер"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_cook",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="Это повар"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(
                blank=True, default=False, verbose_name="Это сотрудник"
            ),
        ),
    ]
