import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vacancies.settings')

app = Celery('vacancies')  
app.config_from_object('django.conf:settings', namespace='CELERY')  

app.autodiscover_tasks()  

app.conf.beat_schedule = {
    'request_vacancies': {
        'task': 'api.tasks.request_vacancies',
        'schedule': crontab(),
        # 'args': (*args)
    },
    'request_candidates': {
        'task': 'api.tasks.request_candidates',
        'schedule': crontab(),
        # 'args': (*args)
    },
}