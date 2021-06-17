from rest_framework import serializers

from main.models import Cashflow, Dish, Transaction, User, DishDateLink


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "cash",
        )


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class DishDateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishDateLink
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    amount = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = "__all__"


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = "__all__"
