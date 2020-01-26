import os

from django.urls import reverse_lazy
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import (
    render,
    redirect, 
    get_object_or_404, 
    reverse
)
from django.views.generic import (
    FormView,
    RedirectView,
    DetailView,
    View,
)
from django.views.generic.edit import FormMixin

from userboard.models import Profile
from userboard.forms import AbilityTestForm
from api.models import Vacancy, AbilityTest



def index(request):
    """
    Индексная страница для отображения списка вакансий и его фильтров
    """
    return render(request, 'userboard/index.html')


class Profile(DetailView):
    """
    Страница профиля. 
    На ней отображены закрепленные за пользователем вакансии
    """
    model = Profile
    template_name = 'userboard/profile/profile.html'


class AddVacToProfile(View):
    """
    Контроллер прикрепления вакансии к профилю
    """
    def post(self, request, *args, **kwargs):
        owner, title = args


class VacancyDetail( DetailView, FormMixin):
    """
    Страница прикрепленной к профилю вакансии. 
    Позволяет прикрепить тест способностей к конкретной вакансии.  
    """
    model = Vacancy
    template_name = 'userboard/vacancy/vacancy.html'
    form_class = AbilityTestForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vac_pk = self.kwargs.get('pk')
        print(vac_pk)
        context['tests'] = AbilityTest.objects.filter(vacancy=vac_pk) 
        context['form'] = self.form_class
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def get_success_url(self):
        vac_pk = {'pk':self.kwargs['pk']}
        return reverse_lazy('userboard:vacancy_detail', kwargs=vac_pk)

    def form_valid(self, form):
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        test = form.save(commit=False)
        test.vacancy = vacancy
        test.save()
        return super().form_valid(form)    


class AbilityTestDownloadView(View):

    """
    Контроллер загрузки вакансии по ссылке. 
    """

    folder_path = settings.MEDIA_ROOT
    file_name = ''
    content_type_value = 'text/plain'

    def get(self, request, file_name, *args, **kwargs):
        self.file_name = file_name
        file_path = os.path.join(self.folder_path, self.file_name)
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(),
                    content_type=self.content_type_value
                )
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
        else:
            raise Http404





