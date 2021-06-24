import datetime
import random

from django.db import transaction
from loguru import logger

from main import models

import factory
from factory.django import DjangoModelFactory

from main.models import IngredientAmount


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("first_name")
    cash = 10000
    is_accountant = True
    is_employee = True
    is_cook = True


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
    measure = "грамм"
    price = 100
    type = factory.SubFactory(IngredientTypeFactory)
    supplier = factory.SubFactory(SupplierFactory)


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


class IngredientAmountFactory(DjangoModelFactory):
    class Meta:
        model = IngredientAmount

    dish = factory.SubFactory(DishFactory)
    ingredient = factory.SubFactory(IngredientFactory)
    amount = 10


class DishWithIngredientsFactory(DishFactory):
    # https://factoryboy.readthedocs.io/en/latest/recipes.html
    # Whenever the DishWithIngredientsFactory is called, it will, as a post-generation hook,
    # call the IngredientAmountFactory, passing the generated dish as a dish field:
    ingredients = factory.RelatedFactory(
        IngredientAmountFactory,
        factory_related_name="dish",
    )


class DishDateLinkFactory(DjangoModelFactory):
    class Meta:
        model = models.DishDateLink

    date = datetime.date.today()
    dish = factory.SubFactory(DishWithIngredientsFactory)


class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = models.Transaction

    amount = 500
    dish_date_link = factory.SubFactory(DishDateLinkFactory)
    user = factory.SubFactory(UserFactory)


@transaction.atomic
def create_data():
    for _ in range(10):
        try:
            TransactionFactory()
        except Exception as e:
            # Plenty things could go wrong, difficult to set particular exception
            logger.debug(e)
            pass
