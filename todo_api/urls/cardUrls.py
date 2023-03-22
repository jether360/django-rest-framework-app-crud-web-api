from django.urls import path
from todo_api.views.cardViews import CardList, CardDetail


urlpatterns = [
    path('', CardList.as_view(), name='card_list'),
    path('<str:pk>/', CardDetail.as_view(), name='card_detail'),
]