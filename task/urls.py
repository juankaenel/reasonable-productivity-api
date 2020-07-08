from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

#define la ruta para los modelos, get,post,put,delet,etc
router = routers.DefaultRouter()
router.register(r'tasks',TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]