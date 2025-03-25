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
        self.fields['username'].help_text = ' '
        
        self.fields['email'].label = 'Электронная почта'
        self.fields['email'].help_text = ' '
        
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = ' '
        
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password2'].help_text = ' '

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Задаем названия полей
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'

class ContactForm(forms.Form):
    name = forms.CharField(label='Введите свое имя', max_length=100)
    tel = forms.CharField(label='Введите ваш номер телефона', max_length=15)
    text = forms.CharField(label='Укажите причину обращения', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name']
        self.fields['tel']
        self.fields['text']