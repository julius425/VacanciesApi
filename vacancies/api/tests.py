from django.test import TestCase
from unittest.mock import patch, Mock
from django.contrib.auth.models import User

from django.conf import settings  
from datetime import datetime

from django.db.models import QuerySet
from .models import Vacancy, Candidate


from .tasks import(
    request_vacancies,
    request_candidates,
)


class TestTasks(TestCase):

    """
    мок тестирование celery-тасков запрос вакансий и кандидатов 
    """

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='admin')
        Vacancy.objects.create(
            id=2,
            title="another_one",
            description="",
            state="ACTIVE",
            owner=None,
        )
    
    @patch('api.tasks.make_vacancies_request')
    def test_vacancies_request(self, mock_make_vacancies_request):
        mock_status_200 = Mock(status_code=200)
        mock_status_200.json.return_value = [{
            "title":"New_vac",
            "description":"",
            "state":"ACTIVE",
            "owner":1
        }]
        mock_make_vacancies_request.return_value = mock_status_200

        response = request_vacancies()

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Vacancy)


    @patch('api.tasks.make_candidates_request')
    def test_vacancies_request(self, mock_make_candidate_request):
        mock_status_200 = Mock(status_code=200)
        mock_status_200.json.return_value = [{
            "vacancy_id": 2,
            "candidate_id": 1,
        }]
        mock_make_candidate_request.return_value = mock_status_200

        response = request_candidates()

        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], Candidate)





