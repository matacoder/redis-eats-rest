from django.urls import path, include

from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
