from django.urls import path
from .views.registration import (
    UserLoginView,
    UserRegisterView,
    UserLogoutView,
)
from .views.userboard import (
    index,
    Profile,
    AddVacToProfile,
    VacancyDetail,
    AbilityTestDownloadView,
)

app_name = 'userboard'

urlpatterns = [
    path('', index, name='index'), 
    path('profile/<slug>/', Profile.as_view(), name='profile'),
    path('profile/add/<owner>/<vac_title>/', AddVacToProfile.as_view(), name='add'),
    path('profile/vacancy/<pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
    path('profile/<slug>/<vac_id>/<file_name>/', AbilityTestDownloadView.as_view(), name='download'),
]

# регистрация
urlpatterns += [
    path('login/', UserLoginView.as_view(), name='login_view'),
    path('register/', UserRegisterView.as_view(), name='register_view'),
    path('logout/', UserLogoutView.as_view(), name='logout_view'),
]