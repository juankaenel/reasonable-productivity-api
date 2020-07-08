from rest_framework import viewsets
from .models import Task
from .serialize import TaskSerializer


#Esta clase me permite realizar el crud
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class= TaskSerializer