from django.contrib import admin
from .models import Task
#https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

class TaskAdmin(admin.ModelAdmin):
    fields = ['title','description'] #cuando ingresamos a una tarea podemos ver estos campos ->http://127.0.0.1:8000/admin/task/task/1/change/
    list_display = ('title','description','created_at','updated_at') #descripcion general de las tareas ->http://127.0.0.1:8000/admin/task/task/

admin.site.register(Task, TaskAdmin)
