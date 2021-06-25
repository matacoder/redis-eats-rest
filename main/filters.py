from django_filters import rest_framework as filters

from main.models import DishDateLink


class DateFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = DishDateLink
        fields = [
            "date",
        ]
