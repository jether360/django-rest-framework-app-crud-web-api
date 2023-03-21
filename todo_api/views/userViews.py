from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from todo_api.serializers.userSerializers import UserSerializer



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

