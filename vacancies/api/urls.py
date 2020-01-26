from django.urls import path, include
from rest_framework import routers

from .views import (
    VacancyViewSet,
    ArchivedVacancyViewSet,
    UserViewSet, 
    state_view_set, 
    VacancyByUserViewSet,
    VacancyByStateViewSet,
    VacancyUpdateView,
    UserVacanciesViewSet,
)

app_name = 'api'

router = routers.DefaultRouter()

router.register('vacancies/all', VacancyViewSet, basename='vacancies')
router.register('vacancies/archived', ArchivedVacancyViewSet, basename='archived_vacancies')
router.register('users/all', UserViewSet, basename='users')
router.register('vacancies/user', VacancyByUserViewSet, basename='by_user')
router.register('vacancies/state', VacancyByStateViewSet, basename='by_state')
router.register('user/vacancies', UserVacanciesViewSet, basename='user_vac')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('states/all/', state_view_set, name='states'),
    path('vacancies/update/<pk>/', VacancyUpdateView.as_view(), name='update')
]
