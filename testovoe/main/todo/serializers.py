from rest_framework import serializers
from .models import TodoListItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = (
            'id',
            'title',
            'desription',
            'date'
        )