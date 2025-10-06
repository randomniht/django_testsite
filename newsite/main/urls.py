from django.urls import path
from .views import * 

urlpatterns = [
    path('', main),
    path('post/', posting),
    path('reg/',registr),
    path('log/', user_login),
    path('logout/', user_logout),
    path('article/<int:pk>/', post_detail, name='post_detail'),
    path('article/<int:pk>/delete/', delete_article, name='delete-article'),
    path('draw/', draw_page),
    path('randphoto/',randmed)
    
]