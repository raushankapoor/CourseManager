from django.db import models
from django.conf import settings
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

