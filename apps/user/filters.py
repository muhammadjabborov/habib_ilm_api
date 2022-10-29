from django_filters.rest_framework import FilterSet, ChoiceFilter

from apps.user.models import Customer


class CustomerFilter(FilterSet):
    class Meta:
        model = Customer
        fields = ['status']
