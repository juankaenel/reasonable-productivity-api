from django.contrib.auth import get_user_model
from django.db import models
from ..utils.models import Timestamps
# Create your models here.

class List(Timestamps,models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)


    #funcion que me permite obtener el nombre de la tarea en la sección de tarea de admin
    def __str__(self):
        return self.name

class ListItem(Timestamps, models.Model):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text