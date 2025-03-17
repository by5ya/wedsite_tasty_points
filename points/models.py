from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.username



class CityOfPoint(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city



class TypeOfPoint(models.Model):
    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name



class Point(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=400)
    type_p = models.ForeignKey(TypeOfPoint, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    city = models.ForeignKey(CityOfPoint, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
    
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'point')  # Один пользователь может лайкнуть точку только один раз

    def __str__(self):
        return f'{self.user.username} likes {self.point.name}'
