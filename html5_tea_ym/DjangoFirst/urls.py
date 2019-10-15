"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from DjangoFirst.views import *
from DjangoFirst.views2 import *
from DjangoFirst.demo_views import *
from DjangoFirst.tea_demo import *
urlpatterns = [
    re_path('about.html/', tem_about_demo),
    re_path('contact.html/', tea_contact_demo),
    re_path('index.html/', tea_index_demo),
    re_path('join.html/', tea_demo),
    re_path('jstore.html/', tea_jstore_demo),
    re_path('news.html/', tea_news_demo),
    re_path('product.html/', tea_demo),

]
