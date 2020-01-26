Описание 
==================
<<<<<<< HEAD
Приложение запрашивающее списки вакансий и кандидатов у стороннего сервиса.

Бэкенд - Django, Django_REST
Фронтенд - JQuery 

=======
Приложение запрашивающее списки вакансий и кандидатов у стороннего REST сервиса.

*   Бэкенд - Django, Django_REST
*   Фронтенд - JQuery 
>>>>>>> 637c8ad5a5e08fbbeb0e05c30ece672208464d66

Установка
===========
1.  Качаем :
    `git clone https://github.com/julius425/VacanciesApi.git`
2.  Настраиваем django :
    1.  Переходим в папку:
        * `cd VacanciesApi`
    2.  Включаем virtualenv и устанавливаем зависимости:
        * `veirtualenv -p python3.6`
        * `. vevnv/bin/activate`
        * `pip install -r requirements.txt`
    3.  Переходим в проект, делаем миграции:
        * `cd vacancies`
        * `./manage.py makemigrations`
        * `./manage.py migrate`
4.  Устанавливаем redis:
    * `apt install redis-server`
    * `redis-server` стартуем
    * `redis-cli ping` пингуем 
5.  В папке с проектом запускаем celery:
    * `# celery -A vacancies worker -B -l info`
