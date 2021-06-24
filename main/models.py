from django.contrib.auth.models import AbstractUser
from django.db import models


class MainSwitch(models.Model):
    is_app_online = models.BooleanField(
        default=True,
        null=False,
        verbose_name="Главный переключатель приложения. Можем оформлять заказы?",
    )

    def __str__(self):
        return f"Главный переключатель ({self.is_app_online})"


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
        return f"{self.get_full_name() or self.username} с балансом: {self.cash}"


class IngredientType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип ингредиента")
    picture = models.ImageField(verbose_name="Изображение типа ингредиента")

    def __str__(self):
        return f"Тип ингредиента: {self.name}"


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя поставщика")
    picture = models.ImageField(verbose_name="Изображение поставщика")
    description = models.TextField(verbose_name="Описание поставщика")
    phone = models.CharField(max_length=100, verbose_name="Телефон поставщика")
    site = models.CharField(max_length=100, verbose_name="Сайт поставщика")
    address = models.CharField(max_length=200, verbose_name="Адрес поставщика")

    def __str__(self):
        return f"Поставщик {self.name}"


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
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Поставщик",
    )

    def __str__(self):
        return f"Ингредиент: {self.name} ({self.measure})"


class DishType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип блюда")
    picture = models.ImageField(verbose_name="Изображение типа блюда")

    def __str__(self):
        return f"Тип блюда {self.name}"


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
    ingredients = models.ManyToManyField(
        Ingredient, related_name="dishes", through="IngredientAmount"
    )

    def __str__(self):
        return f"{self.name} по цене {self.price}"


class IngredientAmount(models.Model):
    """Support model for Ingredient&Recipe ManyToMany relation"""

    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="amounts", verbose_name="Dish"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="amounts",
        verbose_name="Ingredient",
    )
    amount = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Сколько")

    def __str__(self):
        return f"Количество: {self.ingredient.name} by {self.amount}"


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
