from django.urls import path
from todo_api.views.pictureViews import PictureListCreateView

urlpatterns = [
    path('', PictureListCreateView.as_view(), name='picture-list-create'),
]