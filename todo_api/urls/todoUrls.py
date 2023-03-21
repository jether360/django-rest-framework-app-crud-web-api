from django.urls import path
from todo_api.views.todoViews import Todo, TodoDetail


urlpatterns = [
    path('', Todo.as_view()),
    path('<str:pk>', TodoDetail.as_view()),
]