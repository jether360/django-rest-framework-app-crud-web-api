from rest_framework import serializers
from todo_api.models import Book, Author
from todo_api.serializers.authorSerializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(required = True)
    #title = serializers.Field(required=True)

    class Meta:
        model = Book
        fields = '__all__'

    #To validate if the data is already in database either it's in uppercase or lowercase
    def validate_title(self, value):
        if Book.objects.filter(title__iexact=value).exists():
            raise serializers.ValidationError("Title already exists")
        return value
    