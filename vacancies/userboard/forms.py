from django.forms import ModelForm, Textarea, HiddenInput
from django.contrib.auth import authenticate
from django import forms

from .models import User
from api.models.ability_test import AbilityTest


class UserLoginForm(forms.Form):
    """
    Форма логина пользователя
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Пользователь не существует')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
            if not user.is_active:
                raise forms.ValidationError('Пользователь не активен')



class UserRegisterForm(forms.ModelForm):
    """
    Форма регистрации пользователя
    """
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Подтвердите EMail')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if not email == email2:
            raise forms.ValidationError('Имейлы не совпадают')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Имеил уже зарегистрирован')

        return super().clean(*args, **kwargs)



class AbilityTestForm(forms.ModelForm):
    """
    Форма загрузки теста на старнице вакансии
    """
    class Meta:
        model = AbilityTest
        fields = ('is_active', 'description', 'ab_test')