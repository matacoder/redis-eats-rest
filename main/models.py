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
    cash = models.DecimalField(
        decimal_places=2, verbose_name="Баланс", max_digits=19, default=0
    )

    def __str__(self):
        return f"{self.get_full_name()} с балансом: {self.cash}"


class DishType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип блюда")
    picture = models.ImageField(verbose_name="Изображение типа блюда")


class IngredientType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип ингредиента")
    picture = models.ImageField(verbose_name="Изображение типа ингредиента")


class Ingredient(models.Model):
    """Ingredient model"""

    name = models.CharField(max_length=255, verbose_name="Имя ингредиента", unique=True)
    measure = models.CharField(max_length=30, verbose_name="Размерность")
    price = models.DecimalField(
        decimal_places=2, verbose_name="Цена ингредиента", max_digits=10
    )
    type = models.ForeignKey(
        IngredientType,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Тип ингредиента",
    )

    def __str__(self):
        return f"Ingredient: {self.name} ({self.measure})"


class Dish(models.Model):
    name = models.CharField(
        default="New Dish", verbose_name="Имя блюда", max_length=100
    )
    picture = models.ImageField(verbose_name="Изображение блюда")
    description = models.TextField(verbose_name="Описание блюда")
    price = models.DecimalField(
        decimal_places=2, verbose_name="Цена блюда", max_digits=10
    )
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(
        DishType, on_delete=models.SET_DEFAULT, default=None, verbose_name="Тип блюда"
    )

    def __str__(self):
        return f"{self.name} по цене {self.price}"


class DishDateLink(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.SET_DEFAULT, default=None)
    date = models.DateField(verbose_name="Дата планируемой подачи блюда")
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dish.name} запланировано на {self.date}. Готовность: {self.is_ready}"


class Transaction(models.Model):
    dish_date_link = models.ForeignKey(
        DishDateLink,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Дата и блюдо",
    )
    amount = models.DecimalField(
        default=0, decimal_places=2, verbose_name="Сумма транзакции", max_digits=19
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user.cash -= self.amount
        self.user.save()
        super(Transaction, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.cash += self.amount
        self.user.save()
        super(Transaction, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name()} заказал {self.dish_date_link.dish.name} на {self.amount}"


class Cashflow(models.Model):
    amount = models.DecimalField(
        default=0,
        decimal_places=2,
        verbose_name="Введите сумму пополнения",
        max_digits=19,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cashflows")
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user.cash += self.amount
        self.user.save()
        super(Cashflow, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.cash -= self.amount
        self.user.save()
        super(Cashflow, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user.get_full_name()} пополнил счет на {self.amount}"
