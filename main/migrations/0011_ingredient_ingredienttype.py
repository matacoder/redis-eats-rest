# Generated by Django 3.2.3 on 2021-06-21 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_dish_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientType",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Тип ингредиента"),
                ),
                (
                    "picture",
                    models.ImageField(
                        upload_to="", verbose_name="Изображение типа ингредиента"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Имя ингредиента"
                    ),
                ),
                (
                    "measure",
                    models.CharField(max_length=30, verbose_name="Размерность"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена ингредиента"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="main.ingredienttype",
                        verbose_name="Тип ингредиента",
                    ),
                ),
            ],
        ),
    ]
