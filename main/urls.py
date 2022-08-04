from django.urls import path,include
from .views import *
urlpatterns = [
    path('',Index,name = 'index'),
    path('about/', About,name = 'about'),
    path('book/', Book,name = 'book'),
    path('menu/', Menu,name = 'menu'),
]