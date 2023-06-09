from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Todo API built by Jether",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/todo/', include('todo_api.urls.todoUrls')),
    path('api/user/', include('todo_api.urls.userUrls')),
    path('api/book/', include('todo_api.urls.bookUrls')),
    path('api/author/', include('todo_api.urls.authorUrls')),
    path('api/card/', include('todo_api.urls.cardUrls')),
    path('api/picture/', include('todo_api.urls.pictureUrls')),
    path('api/file/', include('todo_api.urls.fileUrls')),
    path('api/upload/', include('todo_api.urls.fileUploadUrls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]