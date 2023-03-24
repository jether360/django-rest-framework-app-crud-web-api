from django.urls import path
from todo_api.views.pictureViews import PictureListCreateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', PictureListCreateView.as_view(), name='picture-list-create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)