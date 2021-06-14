from rest_framework import serializers

from main.models import Cashflow, Dish, Transaction, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class CashflowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cashflow
        fields = "__all__"
