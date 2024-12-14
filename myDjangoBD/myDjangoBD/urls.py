"""
URL configuration for myDjangoBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from django.views.generic import TemplateView
from task1.views import started_func, store_func, buy_func, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', started_func),
    path('store/', store_func),
    path('buy/', buy_func),
    path('django_sign_up/', sign_up_by_django),
]
