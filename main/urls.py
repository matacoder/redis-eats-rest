from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/v1/", include("rest_framework.urls", namespace="rest_framework")),
]

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"dishes", views.DishViewSet)
router.register(r"transactions", views.TransactionViewSet)
router.register(r"cashflows", views.CashflowViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path("api/v1/", include(router.urls)),
]

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
]
