import django_filters
from .models import Sneakers


class SneakerFilter(django_filters.FilterSet):
    model_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Sneakers
        fields = ('model_name', 'model_brand')

