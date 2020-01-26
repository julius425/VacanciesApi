from django.views.generic import FormView, RedirectView
from userboard.forms import UserLoginForm, UserRegisterForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


class UserLoginView(FormView):
    """
    Контроллер логина пользоваетеля
    """
    template_name = 'registration/login.html'
    form_class = UserLoginForm
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return super().form_valid(form)


class UserRegisterView(FormView):
    """
    Контроллер регистрации пользоваетеля
    """
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('/')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class UserLogoutView(RedirectView):
    """
    Контроллер логаута пользоваетеля
    """
    url = '/login/'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)