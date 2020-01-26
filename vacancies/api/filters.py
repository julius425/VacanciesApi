import django_filters
from api.models import Vacancy

class VacancyFilter(django_filters.FilterSet):
    class Meta:
        model = Vacancy
        fields = ['title', 'state', 'owner']