import datetime
import random

from loguru import logger

from main import models

import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("first_name")
    cash = 10000


class IngredientTypeFactory(DjangoModelFactory):
    class Meta:
        model = models.IngredientType

    name = factory.Faker("sentence", nb_words=1, variable_nb_words=True)


class SupplierFactory(DjangoModelFactory):
    class Meta:
        model = models.Supplier

    name = factory.Faker("sentence", nb_words=1, variable_nb_words=True)


class IngredientFactory(DjangoModelFactory):
    class Meta:
        model = models.Ingredient

    name = factory.Faker("sentence", nb_words=1, variable_nb_words=True)


class DishTypeFactory(DjangoModelFactory):
    class Meta:
        model = models.DishType

    name = factory.Faker("sentence", nb_words=1, variable_nb_words=True)


class DishFactory(DjangoModelFactory):
    class Meta:
        model = models.Dish

    name = factory.Faker("sentence", nb_words=1, variable_nb_words=True)
    type = factory.SubFactory(DishTypeFactory)
    price = 600


class DishDateLinkFactory(DjangoModelFactory):
    class Meta:
        model = models.DishDateLink

    date = datetime.date.today()
    dish = factory.SubFactory(DishFactory)


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = models.Transaction
    amount = 500
    dish_date_link = factory.SubFactory(DishDateLinkFactory)
    user = factory.SubFactory(UserFactory)


def create_data():
    for _ in range(10):
        try:
            TransactionFactory()
        except Exception as e:
            logger.debug(e)
            pass
