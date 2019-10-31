from django.db import models


class Quser(models.Model):
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    username = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='image', default='image/头像.jpg')

    identity = models.IntegerField(blank=True, null=False, default=0)






# Create your models here.
