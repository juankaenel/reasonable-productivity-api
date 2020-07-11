from django.contrib.auth import get_user_model
from django.db import models
from ..utils.models import Timestamps
# Create your models here.

class List(Timestamps,models.Model):
    user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)


    #funcion que me permite obtener el nombre de la tarea en la sección de tarea de admin
    def __str__(self):
        return self.name
