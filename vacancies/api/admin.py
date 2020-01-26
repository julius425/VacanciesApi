from django.contrib import admin

from .models.ability_test import AbilityTest
from .models.vacancy import Vacancy
from .models.candidate import Candidate

admin.site.register(Vacancy)
admin.site.register(AbilityTest)
admin.site.register(Candidate)

