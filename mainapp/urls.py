from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('api/getusers', GetProducts.as_view()),
    path('api/register', AddUser.as_view()),
    path('api/works', showWorks.as_view()),

]
