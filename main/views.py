from django.shortcuts import render
from rest_framework import viewsets, permissions

from main.models import User, Dish, Transaction, Cashflow
from main.serializers import UserSerializer, DishSerializer, TransactionSerializer, CashflowSerializer


def index(request):
    return render(request, "index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CashflowViewSet(viewsets.ModelViewSet):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
    permission_classes = [permissions.IsAuthenticated]
