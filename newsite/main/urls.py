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
    path('randphoto/',randmed),
    path('articles/<int:pk>/like/', like_article, name='like_post'),
    path('snake_game/', snake_game),
    path('words/', words,name='words'),
    path('words/<int:word_id>/', words_detail, name='words_detail'),
    path('words/<int:word_id>/delete/', word_delete, name='word_delete')
]
