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


class GoodsAddress(models.Model):
    """
    收货地址
    """
    recver = models.CharField(max_length=64)
    address = models.TextField()
    post_number = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    state = models.IntegerField()  # 0代表常规地址  1 默认地址

    user = models.ForeignKey(to=Quser, on_delete=models.CASCADE, default=4)
# Create your models here.
