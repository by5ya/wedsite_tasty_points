
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление после успешной регистрации
    else:
        form = RegisterForm()  # Создаем пустую форму для GET-запроса
    return render(request, 'registration_page.html', {'form': form})  # Передаем форму в шаблон

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление после успешной авторизации
    else:
        form = LoginForm()  # Создаем пустую форму для GET-запроса
    return render(request, 'login.html', {'form': form})  # Передаем форму в шаблон

def home_page(request):
    return render(request, 'index.html')  

def point_page(request):
    return render(request, 'points.html')

def contact_page(request):
    return render(request, 'contacts.html')

def registration_page(request):
    return render(request, 'registration_page.html')
def login_page(request):
    return render(request, 'login.html')
