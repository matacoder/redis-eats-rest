from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

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

schema_view = get_swagger_view(title="Pastebin API")

urlpatterns += [path("swagger/", schema_view)]
