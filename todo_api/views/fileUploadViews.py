from rest_framework.parsers import FileUploadParser, FormParser , MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , generics, serializers
from todo_api.models import FileUpload
from todo_api.serializers.fileUploadSerializers import FileSerializer



class FileUploadView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)