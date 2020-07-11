#django
from django.db import models
from django.contrib.auth import get_user_model
#local
from ..utils.models import Timestamps

class Task(Timestamps,models.Model):
    user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, null=True)


    #funcion que me permite obtener el nombre de la tarea en la sección de tarea de admin
    def __str__(self):
        return self.title
