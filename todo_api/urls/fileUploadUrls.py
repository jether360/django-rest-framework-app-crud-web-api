from django.urls import path
from todo_api.views.fileUploadViews import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
]