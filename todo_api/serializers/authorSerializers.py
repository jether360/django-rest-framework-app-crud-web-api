from rest_framework import serializers
from todo_api.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    #name = serializers.Field(required=True)

    class Meta:
        model = Author
        fields = '__all__'



