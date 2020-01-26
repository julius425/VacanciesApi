from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import(
    ListAPIView,
    UpdateAPIView,
    GenericAPIView
)
from rest_framework.mixins import UpdateModelMixin 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from .serializers import VacancySerializer, UserSerializer
from .models.vacancy import Vacancy
from .filters import VacancyFilter
from userboard.models import User


class VacancyViewSet(viewsets.ModelViewSet):
    """
    Фильтр всех активных(неархивированных) вакансий
    """
    queryset = Vacancy.filter_non_archived()
    serializer_class = VacancySerializer


class ArchivedVacancyViewSet(viewsets.ModelViewSet):
    """
    Фильтр вакансий из архива
    """
    queryset = Vacancy.filter_archived()
    serializer_class = VacancySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Список пользователей(drop-down меню)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view()
def state_view_set(request):
    """
    Список всех статусов(drop-down меню)
    """
    qs = Vacancy.get_all_states()
    return Response(qs)


class VacancyByUserViewSet(viewsets.ModelViewSet):
    """
    Фильтр вакансий по конкретному пользователю
    """
    serializer_class = VacancySerializer

    def get_queryset(self):
        username = self.request.GET.get('username')
        print(username)
        qs = Vacancy.filter_by_owner(username)
        return qs


class VacancyByStateViewSet(viewsets.ModelViewSet):
    """
    Фильтр вакансий по статусу
    """
    serializer_class = VacancySerializer

    def get_queryset(self):
        state = self.request.GET.get('state')
        qs = Vacancy.filter_by_state(state)
        return qs


class UserVacanciesViewSet(viewsets.ModelViewSet):
    """
    Фильтр вакансий по конкретному пользователю на странице пофиля 
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
    def get_queryset(self):
        user = self.request.user
        return Vacancy.get_user_vacancies(user)

    def get(self, request, *args, **kwargs):
        vacancies = self.get_queryset()
        serializer = self.serializer_class(vacancies)
        return Response(serializer.data)


class VacancyUpdateView(GenericAPIView, UpdateModelMixin):
    """
    Контроллер обновления вакансии 
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def patch(self, request, pk=None):
        vacancy = Vacancy.objects.get(pk=pk)
        user_pk = request.data.get('owner')
        if user_pk:
            vacancy.owner = User.objects.get(pk=user_pk)
        else:
            vacancy.owner = None

        serialized_data = self.serializer_class(vacancy, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)