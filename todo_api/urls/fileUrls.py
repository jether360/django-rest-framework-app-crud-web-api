from django.urls import path
from todo_api.views.fileViews import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
    #path('', FileListView.as_view()),
]