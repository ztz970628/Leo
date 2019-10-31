from django.urls import path, re_path
from Shop.views import *
"""
    配置子路由
"""
urlpatterns = [
    re_path(r'^$', index),
    path('index/', index),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('forget_password/', forget_password),
    path('reset_password/', reset_password),
    path('change_password/', change_password),
    path('profile/', profile),
    path('list_goods/', list_goods),
    re_path(r"^set_goods/(?P<id>\d+)/", set_goods),
    re_path(r"^goods/(?P<id>\d+)/", goods),
    path('set_profile/', set_profile),
]

urlpatterns += [
    path('get_celery/', get_celery),

    path('add_update_goods/', add_update_goods),
    re_path(r"add_update_goods/(?P<id>\d+)/", add_update_goods),


    path('Goods/', GoodsView.as_view()),
    path('vue_list_goods/', vue_list_goods)
]