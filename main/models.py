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

    def __str__(self):
        return f"{self.name} по цене {self.price}"


class Transaction(models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.SET_DEFAULT, default=None, verbose_name="Блюдо"
    )
    amount = models.DecimalField(
        default=0, decimal_places=2, verbose_name="Покупка блюда", max_digits=19
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return f"{self.user.get_full_name()} заказал {self.dish.name} на {self.amount}"


class Cashflow(models.Model):
    amount = models.DecimalField(
        default=0, decimal_places=2, verbose_name="Пополнение счета", max_digits=19
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.user.cash += self.amount
        self.user.save()
        super(Cashflow, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.cash -= self.amount
        self.user.save()
        super(Cashflow, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user} пополнил счет на {self.amount}"
