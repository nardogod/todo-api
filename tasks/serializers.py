from rest_framework import serializers
from .models import Task

class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "completed", "created_at"]
#code:ignore