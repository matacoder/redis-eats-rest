from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_accountant = models.BooleanField(
        default=False, verbose_name="Это бухгалтер", blank=True
    )
    is_employee = models.BooleanField(
        default=False, verbose_name="Это сотрудник", blank=True
    )
    is_cook = models.BooleanField(default=False, verbose_name="Это повар", blank=True)


class Dish(models.Model):
    name = models.CharField(
        default="New Dish", verbose_name="Имя блюда", max_length=100
    )
    picture = models.ImageField(verbose_name="Изображение блюда")
    description = models.TextField(verbose_name="Описание блюда")
    price = models.DecimalField(
        decimal_places=2, verbose_name="Цена блюда", max_digits=10
    )
