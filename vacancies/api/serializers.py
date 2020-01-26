from rest_framework import serializers
from .models.vacancy import Vacancy
from userboard.models import User


class VacancySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username', default='отсутствует')
    
    class Meta:
        model = Vacancy
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


