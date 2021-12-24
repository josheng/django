from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # assuming this is ref to views file with index method, first arg is route
    path('test', views.test, name='test'), # have to define a route name, name arg is probably like rails route name
]
