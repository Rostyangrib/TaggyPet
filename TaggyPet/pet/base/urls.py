
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_home, name = 'base_home'),
    path('create', views.create, name = 'create'),
]
