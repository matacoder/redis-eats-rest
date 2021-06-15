from django.shortcuts import get_object_or_404, render
from rest_framework import permissions, viewsets

from main.models import Cashflow, Dish, Transaction, User
from main.permissions import (
    AccountantPermission,
    CookPermissionOrReadOnly,
    IsOwnerOrAccountantPermission,
    ReadOnly,
)
from main.serializers import (
    CashflowSerializer,
    DishSerializer,
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
    permission_classes = [permissions.IsAuthenticated, ReadOnly]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated, CookPermissionOrReadOnly]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAccountantPermission]

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
