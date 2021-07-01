from django_filters import rest_framework as filters

from main.models import DishDateLink, Transaction


class DishDateLinkFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = DishDateLink
        fields = [
            "date",
        ]


class TransactionFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name="dish_date_link__date")
    user = filters.CharFilter(field_name="user__username")


class IngredientFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name="dishes__dish_date_links__date")
