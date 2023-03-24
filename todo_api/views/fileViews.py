from rest_framework.parsers import FileUploadParser, FormParser , MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , generics
from todo_api.models import File
from todo_api.serializers.fileSerializers import FilePostSerializer, FileGetSerializer

class FileUploadView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FilePostSerializer
    parser_class = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FilePostSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class FileListView(APIView):
    #def get(self, request):
        #files = File.objects.all()
        #serializer = FileGetSerializer(files, many=True)
        #return Response(serializer.data)

