from django.contrib import admin
from .models import CustomUser, Point, TypeOfPoint, CityOfPoint, Like
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(TypeOfPoint)
admin.site.register(Point)
admin.site.register(CityOfPoint)
admin.site.register(Like)