from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from todo_api.models import Picture
from todo_api.serializers.pictureSerializers import PictureSerializer


class PictureListCreateView(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    parser_classes = (MultiPartParser, FormParser)