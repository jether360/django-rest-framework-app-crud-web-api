from rest_framework import serializers
from todo_api.models import File

#this serializer is for post method
class FilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'filename', 'file')

#this serializer is for get method
class FileGetSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id', 'name', 'file', 'file_url')

    def get_file_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.file.url)

