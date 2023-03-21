from rest_framework import generics, status
from rest_framework.response import Response
import math
from datetime import datetime
from todo_api.models import Book
from drf_yasg.utils import swagger_auto_schema
from todo_api.serializers.bookSerializers import BookSerializer


class BookList(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        book = Book.objects.all()
        total_books = book.count()
        if search_param:
            book = book.filter(title__icontains=search_param)
        serializer = self.serializer_class(book[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_books,
            "page": page_num,
            "last_page": math.ceil(total_books / limit_num),
            "book": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "book": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_note(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        book = self.get_note(pk=pk)
        if book == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(book)
        return Response({"status": "success", "book": serializer.data})

    def put(self, request, pk):
        book = self.get_note(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "book": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_note(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Book with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
