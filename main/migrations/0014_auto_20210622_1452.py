# Generated by Django 3.2.3 on 2021-06-22 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_mainswitch"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientAmount",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=1, max_digits=5, verbose_name="Сколько"
                    ),
                ),
                (
                    "dish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="amounts",
                        to="main.dish",
                        verbose_name="Dish",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="amounts",
                        to="main.ingredient",
                        verbose_name="Ingredient",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dish",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="dishes",
                through="main.IngredientAmount",
                to="main.Ingredient",
            ),
        ),
    ]
