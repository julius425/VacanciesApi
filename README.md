Описание 
==================
Приложение запрашивающее списки вакансий и кандидатов у стороннего REST сервиса.

*   Бэкенд - Django, Django_REST
*   Фронтенд - JQuery 


Установка
===========
1.  Качаем :
    `git clone https://github.com/julius425/VacanciesApi.git`
2.  Настраиваем django :
    1.  Переходим в папку:
        * `cd VacanciesApi`
    2.  Включаем virtualenv и устанавливаем зависимости:
        * `veirtualenv -p python3.6 venv`
        * `. venv/bin/activate`
        * `pip install -r requirements.txt`
    3.  Переходим в проект, делаем миграции:
        * `cd vacancies`
        * `./manage.py migrate`
4.  Устанавливаем redis:
    * `apt install redis-server`
    * `redis-server` стартуем
    * `redis-cli ping` пингуем 
5.  В папке с проектом запускаем celery:
    * `# celery -A vacancies worker -B -l info`
