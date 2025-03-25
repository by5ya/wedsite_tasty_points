
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm, ContactForm
from .models import CityOfPoint, Point, TypeOfPoint
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Like, Point
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt

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

def get_points(request):
    city_filter = request.GET.get('city')  # Получаем параметр фильтрации по городу
    type_filter = request.GET.get('type')  # Получаем параметр фильтрации по типу ресторана

    points = Point.objects.all()

    # Фильтрация по городу
    if city_filter:
        points = points.filter(city__id=city_filter)  # Фильтруем по ID города

    # Фильтрация по типу ресторана
    if type_filter:
        points = points.filter(type_p__id=type_filter)  # Фильтруем по ID типа ресторана

    # Получаем все города и типы для отображения в форме
    cities = CityOfPoint.objects.all()
    types = TypeOfPoint.objects.all()
    if request.user.is_authenticated:
        # Получаем ID всех точек, которые лайкнул текущий пользователь
        liked_points = Like.objects.filter(user=request.user).values_list('point_id', flat=True)
        return render(request, 'points.html', {
        'points': points,
        'liked_points': liked_points,
        'cities': cities,
        'types': types,
        })
    else:
        return render(request, 'points.html', {
        'points': points,
        'cities': cities,
        'types': types,
        })

    

@login_required
@require_POST
def like_point(request, point_id):
    point = Point.objects.get(id=point_id)
    user = request.user

    try:
        # Пытаемся создать лайк, если его еще нет
        like, created = Like.objects.get_or_create(user=user, point=point)
        if not created:
            # Если лайк уже существует, удаляем его
            like.delete()
            liked = False
        else:
            # Если лайк создан, устанавливаем liked = True
            liked = True
    except Exception as e:
        # Логируем ошибку и возвращаем сообщение об ошибке
        print(f"Error: {e}")
        return JsonResponse({'error': 'An error occurred'}, status=500)

    return JsonResponse({'liked': liked})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            text = form.cleaned_data['text']
            subject = f'Новое сообщение от {name}'
            message = f'Имя: {name}\nТелефон: {tel}\nСообщение: {text}'
            send_mail(subject, message, 'tigriska2006@mail.ru', ['tigriska2006@mail.ru'])  # Замените на ваш email
            return render(request, 'contacts.html', {'form': ContactForm()})  # Страница успеха
    else:
        form = ContactForm()
    
    return render(request, 'contacts.html', {'form': form})