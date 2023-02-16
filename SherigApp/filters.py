import django_filters
from .models import *
from django_filters import CharFilter, NumberFilter


class StaffFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    Employee_ID = NumberFilter(
        field_name='Employee_ID', lookup_expr='icontains')

    class Meta:
        model = StaffDetail
        fields = [
            'category',
            'name',
            'Employee_ID',
            
        ]

class topperFilter(django_filters.FilterSet):
    class Meta:
        model = TopperOfYear
        fields = [
            'standard',
            'subject',
        ]


