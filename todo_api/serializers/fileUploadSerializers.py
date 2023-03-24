from rest_framework import serializers
from todo_api.models import FileUpload

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'