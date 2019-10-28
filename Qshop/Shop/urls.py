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
]

urlpatterns += [
    path('get_celery/', get_celery),
    path('profile/', profile),
    path('set_profile/', set_profile),
]