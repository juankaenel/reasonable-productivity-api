from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #funcion que me permite obtener el nombre de la tarea en la sección de tarea de admin
    def __str__(self):
        return self.title
