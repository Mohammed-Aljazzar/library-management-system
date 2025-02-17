from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    
]