from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('users/login', login),
    path('users/logout', logout)


]