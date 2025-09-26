from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'mark': ['exact'],
            'year': ['gte', 'lte'],
            'price': ['gte', 'lte'],
            'model': ['exact'],
            'paint_color': ['exact']
        }