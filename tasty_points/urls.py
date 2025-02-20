"""
URL configuration for tasty_points project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from points.views import home_page, point_page, contact_page, registration_page, login_page
from points import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('points/', point_page, name="point"),
    path('contacts/', contact_page, name="contacts"),
    path('register/', views.register, name='register'),  # Важно, чтобы этот URL был правильным
    path('login/', views.user_login, name='login'),
    #path('registration_page/', registration_page, name="registration"),
    #path('log-in/', login_page, name="login"),
]