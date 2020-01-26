import requests
from .models import Vacancy, Candidate
from userboard.models import User


def create_vacancy(vac):
    """
    Создаем новую вакансию 
    """
    # vac_id = vac.get('id')
    vac_title = vac.get('title')
    vac_state = vac.get('state')
    vac_owner_id = vac.get('owner')

    vac['owner'] = User.objects.get(pk=vac_owner_id) 

    try:
        vacancy = Vacancy.objects.get(title=vac_title)
        if vacancy:
            vacancy.state = vac_state
            vacancy.save()
            return vacancy

    except Vacancy.DoesNotExist:

        vacancy = Vacancy.objects.create(**vac)
        print(vacancy)
        vacancy.save()
        return vacancy

    
def check_archived(data):
    """
    Архивируем невошедшие в список вакансии
    """
    recived_ids = [v_id.get('id') for v_id in data]
    to_archive = Vacancy.objects.exclude(id__in=recived_ids).update(state='ARCHIVE')
    
    # print(to_archive)

    return f'{to_archive} vacancies archived.'


def create_candidate(can):
    """
    создаем нового кандидата 
    """

    vac_id = can['vacancy_id']
    can_id = can['candidate_id']
    vacancy = Vacancy.objects.get(pk=vac_id)
    
    if vacancy.candidate.filter(candidate_id=can_id).exists():
        return 'double'

    candidate = Candidate.objects.create(
        vacancy = vacancy,
        candidate_id=can_id
    )
    candidate.save()

    return candidate
