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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    re_path(r'func/?address=(?P<month>\d{1,2})&address=(?P<day>\d{1,2})', ages_num),
    re_path('windmill/', windmill)
    # re_path('func/', func),

]
