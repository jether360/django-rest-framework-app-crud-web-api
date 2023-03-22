from rest_framework import serializers
from todo_api.models import Author
from todo_api.serializers.cardSerializers import CardSerializer

#serializers is just like a response you can modify the field, you want to display in get method
class AuthorSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields =  ['id', 'name', 'cards']



