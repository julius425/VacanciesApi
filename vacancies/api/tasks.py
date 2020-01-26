import requests
from vacancies.celery import app
from django.conf import settings
from collections import defaultdict
from .task_utils import (
    create_vacancy,
    check_archived,
    create_candidate,
)


def make_vacancies_request():
    return requests.get(settings.VAC_HOST_URL)

def make_candidates_request():
    return requests.get(settings.CAN_HOST_URL)



@app.task
def request_vacancies():
    """
    Запрашиваем у хоста новые вакансии. (крон 30 сек по дефолту.)
    Создаем вакансии из полученного списка. 
    Помещаем в архив отсутствующие в списке вакансии. 
    """
    response = make_vacancies_request()
    data = response.json()

    created = []
    
    for vac in data:
        new_vacancy = create_vacancy(vac)
        created.append(new_vacancy)

    check_archived(data)
    return created


@app.task
def request_candidates():
    """
    Запрашиваем и создаем новых кандидатов
    """
    response = make_candidates_request()
    data = response.json()

    created = []
    
    for can in data:
        new_candidate = create_candidate(can)
        created.append(new_candidate)

    return created