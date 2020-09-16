"""recetario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from recetasapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page,name='home'),
    path('flor/', views.florcalab,name='flor'),
    path('canelon/', views.canelon,name='canelon'),
    path('pizza/', views.pizza, name='pizza'),
    path('carbonara/', views.carbonara, name='carbonara'),
    path('ensaladilla/', views.ensaladilla, name='ensaladilla'),
    path('feijoada/', views.feijoada, name='feijoada'),
    path('gazpacho/', views.gazpacho, name='gazpacho'),
    path('mafe/', views.mafe, name='mafe'),
    path('menuinf/', views.menuinf, name='menuinf'),
    path('recetafacil/', views.recetafacil, name='recetafacil'),
    path('noodles/', views.noodles, name='noodles'),

]

