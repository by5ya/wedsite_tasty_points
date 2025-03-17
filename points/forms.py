from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Задаем названия полей
        self.fields['username'].label = 'Имя пользователя'
        self.fields['username'].help_text = 'Придумайте уникальное имя пользователя.'
        
        self.fields['email'].label = 'Электронная почта'
        self.fields['email'].help_text = 'Введите ваш email.'
        
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = 'Пароль должен содержать не менее 8 символов.'
        
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = 'Повторите пароль для подтверждения.'

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Задаем названия полей
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'