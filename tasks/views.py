from rest_framework import viewsets
from .models import Task
from .serializers import todoserializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = todoserializer
