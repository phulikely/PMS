import django_filters
from django_filters import DateFilter
from django_filters.filters import CharFilter

from .models import *

class ProjectFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    # name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['customer', 'date_created', ]