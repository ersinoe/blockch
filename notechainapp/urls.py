from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="notechainapp-home"),
    path('about/', views.about, name="notechainapp-about"),
]