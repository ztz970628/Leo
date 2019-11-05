from django.db import models
from ckeditor.fields import RichTextField
from QUser.models import *


class GoodsType(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='shop/img', default='shop/img/1.jpg')


class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    number = models.IntegerField()
    production = models.DateTimeField()
    safe_date = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='shop/img', default='shop/img/1.jpg')
    description = RichTextField()

    statue = models.IntegerField(default=1)  # 0下架  1下架

    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE)
    goods_store = models.ForeignKey(to=Quser, on_delete=models.CASCADE)
# Create your models here.
