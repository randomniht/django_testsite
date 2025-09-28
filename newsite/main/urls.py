from django.urls import path
from .views import * 

urlpatterns = [
    path('', main),
    path('post/', posting),
    path('reg/',registr),
    path('log/', user_login),
    path('logout/', user_logout)
    
]