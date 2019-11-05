from django.urls import path, re_path
from Buyer.views import *

urlpatterns = [
    path('index/', index),
    path('', index),
    path('cart/', cart),
    path('login/', login),
    path('logout/', logout),
    path('add_car/', add_car),
    path('place_order/', place_order),
    path('user_center_info/', user_center_info),
    path('user_center_site/', user_center_site),
    re_path(r'list/(?P<id>\d+)', goods_list),
    re_path(r'good_data/(?P<id>\d+)', good_data),
    re_path(r"^$", index),
]