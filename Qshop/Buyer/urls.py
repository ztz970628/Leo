from django.urls import path, re_path
from Buyer.views import *

urlpatterns = [
    path('index/', index),
    path('', index),
    re_path(r'list/(?P<id>\d+)', goods_list),
    re_path(r'good_data/(?P<id>\d+)', good_data ),
    re_path(r"^$", index),
]