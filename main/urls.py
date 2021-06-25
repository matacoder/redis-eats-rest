from django.conf.urls import url
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/", include("rest_framework.urls", namespace="rest_framework")),
]

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"permissions", views.UserPermissionViewSet)
router.register(r"dishes", views.DishViewSet)
router.register(r"dish-date-links", views.DishDateLinkViewSet)
router.register(r"transactions", views.TransactionViewSet)
router.register(r"full-data-transactions", views.FullDataTransactionViewSet)
router.register(r"cash-flows", views.CashflowViewSet)
router.register(r"dish-types", views.DishTypeViewSet)
router.register(r"suppliers", views.SupplierViewSet)
router.register(r"ingredients", views.IngredientViewSet)
router.register(r"ingredient-types", views.IngredientTypeViewSet)
router.register(r"devices", FCMDeviceAuthorizedViewSet)

# API v1
urlpatterns += [
    path("api/v1/", include(router.urls)),
]

# Swagger/ReDoc
urlpatterns += [
    # YOUR PATTERNS
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    url("control/", views.control_panel, name="control"),
    url("delete/", views.delete_orders, name="delete_orders"),
    url("create-fake-data/", views.create_fake_data, name="fake"),
]

# SimpleJWT
urlpatterns += [
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
