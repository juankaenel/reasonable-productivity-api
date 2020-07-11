from .models import List
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'