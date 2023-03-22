from rest_framework import serializers
from todo_api.models import Cards

#This serializers to modify the specific field i want to display in my views
class CardViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields =  ['id', 'cards','author']



#this serializers is use in author serializers to display my cards in author instance
class CardSerializer(serializers.ModelSerializer):
    #name = serializers.Field(required=True)

    class Meta:
        model = Cards
        fields =  ['id', 'cards']