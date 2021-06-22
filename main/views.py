from django.shortcuts import get_object_or_404, render
from rest_framework import permissions, viewsets

from main.models import (
    Cashflow,
    Dish,
    DishDateLink,
    DishType,
    Ingredient,
    IngredientType,
    Supplier,
    Transaction,
    User,
)
from main.permissions import (
    AccountantPermission,
    CookPermissionOrReadOnly,
    IsOwnerOrAccountantPermission,
    MainSwitchPermission,
    ReadOnly,
)
from main.serializers import (
    CashflowSerializer,
    DishDateLinkSerializer,
    DishSerializer,
    DishTypeSerializer,
    IngredientSerializer,
    IngredientTypeSerializer,
    SupplierSerializer,
    TransactionSerializer,
    UserSerializer,
)


def index(request):
    return render(request, "index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnly, MainSwitchPermission]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class DishTypeViewSet(viewsets.ModelViewSet):
    queryset = DishType.objects.all()
    serializer_class = DishTypeSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class IngredientTypeViewSet(viewsets.ModelViewSet):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class DishDateLinkViewSet(viewsets.ModelViewSet):
    queryset = DishDateLink.objects.all()
    serializer_class = DishDateLinkSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrAccountantPermission,
        MainSwitchPermission,
    ]

    def perform_create(self, serializer):
        dish_id = int(self.request.data.get("dish"))
        dish = get_object_or_404(Dish, id=dish_id)
        serializer.save(
            amount=dish.price,
            user=self.request.user,
        )


class CashflowViewSet(viewsets.ModelViewSet):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
    permission_classes = [permissions.IsAuthenticated, AccountantPermission]
