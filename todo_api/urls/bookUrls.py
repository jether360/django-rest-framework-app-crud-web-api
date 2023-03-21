from django.urls import path
from todo_api.views.bookViews import BookList, BookDetail


urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<str:pk>/', BookDetail.as_view(), name='book_detail'),
]