from .models import List, ListItem
from rest_framework import serializers

# esta clase nos permitira transportar nuestros objetos a traves de la red por el protocolo http, ya sea formato json o otros
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField(
            queryset=List.objects.all())

    class Meta:
        model = ListItem
        fields = ['id', 'text', 'parent_list',
                  'created_at', 'updated_at']