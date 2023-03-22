from rest_framework import generics, status
from rest_framework.response import Response
import math
from datetime import datetime
from todo_api.models import Cards
from todo_api.serializers.cardSerializers import CardSerializer, CardViewsSerializer


class CardList(generics.GenericAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardViewsSerializer

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        card = Cards.objects.all()
        total_cards = card.count()
        if search_param:
            card = card.filter(title__icontains=search_param)
        serializer = self.serializer_class(card[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_cards,
            "page": page_num,
            "last_page": math.ceil(total_cards / limit_num),
            "cards": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "card": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(generics.GenericAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardViewsSerializer

    def get_note(self, pk):
        try:
            return Cards.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        card = self.get_note(pk=pk)
        if card == None:
            return Response({"status": "fail", "message": f"Card with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(card)
        return Response({"status": "success", "book": serializer.data})

    def put(self, request, pk):
        card = self.get_note(pk)
        if card == None:
            return Response({"status": "fail", "message": f"Card with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            card, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "card": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_note(pk)
        if card == None:
            return Response({"status": "fail", "message": f"Card with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)