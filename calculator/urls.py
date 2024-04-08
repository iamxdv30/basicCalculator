from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('basic', views.index, name='index'),
]