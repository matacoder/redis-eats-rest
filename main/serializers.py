from rest_framework import serializers

from main.models import (
    Cashflow,
    Dish,
    DishDateLink,
    DishType,
    Ingredient,
    IngredientType,
    Supplier,
    Transaction,
    User, IngredientAmount,
)


class DishSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = "__all__"


class DishTypeSerializer(DishTypeBasicSerializer):
    dishes = DishSerializerBasic(many=True)


class IngredientBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientTypeBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientType
        fields = "__all__"


class IngredientTypeSerializer(IngredientTypeBasicSerializer):
    ingredients = IngredientBasicSerializer(many=True)


class SupplierBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierSerializer(SupplierBasicSerializer):
    ingredients = IngredientBasicSerializer(many=True)


class IngredientSerializer(IngredientBasicSerializer):
    type = IngredientTypeBasicSerializer()
    supplier = SupplierBasicSerializer()


class IngredientAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientAmount
        fields = "__all__"


class IngredientSumSerializer(serializers.Serializer):
    # amounts = IngredientAmountSerializer(many=True, read_only=True)
    name = serializers.CharField(max_length=200)
    sum = serializers.DecimalField(decimal_places=2, max_digits=19)


class DishSerializer(DishSerializerBasic):
    ingredients = IngredientSerializer(many=True)
    type = DishTypeBasicSerializer()


class DishDateLinkSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = DishDateLink
        fields = "__all__"


class DishDateLinkReadySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishDateLink
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    amount = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = "__all__"


class FullDataTransactionSerializer(serializers.ModelSerializer):
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
    cash = serializers.ReadOnlyField()

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
            "position",
            "is_accountant",
            "is_employee",
            "is_cook",
            "is_notify",
        )


class UserPermissionSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    cash = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "cash",
            "is_accountant",
            "is_employee",
            "is_cook",
            "is_notify",
        )
