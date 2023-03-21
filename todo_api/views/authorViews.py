from rest_framework import generics, status
from rest_framework.response import Response
import math
from datetime import datetime
from todo_api.models import Author
from todo_api.serializers.authorSerializers import AuthorSerializer


class AuthorList(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        author = Author.objects.all()
        total_notes = author.count()
        if search_param:
            author = author.filter(title__icontains=search_param)
        serializer = self.serializer_class(author[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "last_page": math.ceil(total_notes / limit_num),
            "author": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "author": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_note(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        author = self.get_note(pk=pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(author)
        return Response({"status": "success", "book": serializer.data})

    def put(self, request, pk):
        author = self.get_note(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "author": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_note(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)