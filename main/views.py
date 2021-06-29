import django_filters
from loguru import logger

from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import permissions, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from main.filters import DishDateLinkFilter, TransactionFilter
from main.generate_data import create_data
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
    MainSwitch,
)
from main.permissions import (
    AccountantPermission,
    CookPermissionOrReadOnly,
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
    UserPermissionSerializer,
    FullDataTransactionSerializer,
    DishDateLinkReadySerializer,
)
from main.services import get_main_switch_status, delete_orders_logic


def index(request):
    return render(request, "index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ReadOnly, MainSwitchPermission]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [
        "username",
        "first_name",
        "last_name",
    ]


class UserPermissionViewSet(
    viewsets.GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserPermissionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        MainSwitchPermission,
    ]


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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [
        "type__name",
        "price",
        "supplier",
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
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_class = DishDateLinkFilter
    filterset_fields = [
        "date",
    ]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        MainSwitchPermission,
    ]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TransactionFilter

    def perform_create(self, serializer):
        dish_id = int(self.request.data.get("dish"))
        dish = get_object_or_404(Dish, id=dish_id)
        serializer.save(
            amount=dish.price,
            user=self.request.user,
        )


class FullDataTransactionViewSet(
    viewsets.GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    queryset = Transaction.objects.all()
    serializer_class = FullDataTransactionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TransactionFilter


class CashflowViewSet(viewsets.ModelViewSet):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
    permission_classes = [permissions.IsAuthenticated, AccountantPermission]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


def control_panel(request):
    data = dict()
    data["main_switch"] = get_main_switch_status()
    if request.method == "POST":
        if request.POST.get("switch"):
            switch = MainSwitch.objects.latest("id")
            if data["main_switch"]:
                switch.is_app_online = False
            else:
                switch.is_app_online = True
            switch.save()
    data["main_switch"] = get_main_switch_status()
    return render(request, template_name="control.html", context=data)


def delete_orders(request):
    date = str(request.POST.get("from"))
    logger.debug(date)
    delete_orders_logic(date)
    return redirect("control")


def create_fake_data(request):
    create_data()
    return redirect("control")


class DishDateLinkReadyViewSet(viewsets.ModelViewSet):
    queryset = DishDateLink.objects.all()
    serializer_class = DishDateLinkReadySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        CookPermissionOrReadOnly,
        MainSwitchPermission,
    ]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_class = DishDateLinkFilter
    filterset_fields = [
        "date",
    ]
