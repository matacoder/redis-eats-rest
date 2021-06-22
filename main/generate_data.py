import random

from main import models

import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("first_name")


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


def create_data():
    for _ in range(10):
        UserFactory(cash=random.randint(1000, 2000))
