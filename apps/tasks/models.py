#django
from django.db import models
from django.contrib.auth import get_user_model
#local
from ..utils.models import Timestamps

class Task(Timestamps,models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField(default='', blank=True) #blank true es para que pueda enviarse vacío desde el front
    completed = models.BooleanField(default=False)


    #funcion que me permite obtener el nombre de la tarea en la sección de tarea de admin
    def __str__(self):
        return self.title
