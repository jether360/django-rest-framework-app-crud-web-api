from rest_framework import serializers
from todo_api.models import TBL_TODO


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBL_TODO
        fields = '__all__'


