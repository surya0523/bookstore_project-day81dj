from django.urls import path
from . import views

urlpatterns = [
    # General app views
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),

    # New login/register views
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]