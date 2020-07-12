from rest_framework import viewsets
from .models import List, ListItem
from .serialize import ListSerializer, ListItemSerializer


#Esta clase me permite realizar el crud
class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class= ListSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer