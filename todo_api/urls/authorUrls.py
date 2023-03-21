from django.urls import path
from todo_api.views.authorViews import AuthorList, AuthorDetail


urlpatterns = [
    path('', AuthorList.as_view(), name='book_list'),
    path('<str:pk>/', AuthorDetail.as_view(), name='book_detail'),
]