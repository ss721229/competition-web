from django.urls import path
from mainpage import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.index),
]