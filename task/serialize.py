from .models import Task
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'