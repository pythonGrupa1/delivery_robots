from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='pizzeria-home'),
    path('about/', views.about, name='pizzeria-about')
]