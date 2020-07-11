from rest_framework import viewsets
from .models import List
from .serialize import ListSerializer


#Esta clase me permite realizar el crud
class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class= ListSerializer