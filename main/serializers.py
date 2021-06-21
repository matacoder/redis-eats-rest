from rest_framework import serializers

from main.models import (
    Cashflow,
    Dish,
    DishDateLink,
    Transaction,
    User,
    DishType,
    IngredientType,
    Supplier,
    Ingredient,
)


class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = "__all__"


class IngredientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    type = IngredientTypeSerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Ingredient
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    type = DishTypeSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = "__all__"


class DishDateLinkSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = DishDateLink
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )
    amount = serializers.ReadOnlyField()
    dish_date_link = DishDateLinkSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"


class CashflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashflow
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    cashflows = CashflowSerializer(many=True, read_only=True)
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "cash",
            "cashflows",
            "transactions",
        )
