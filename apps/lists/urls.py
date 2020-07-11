from django.urls import path, include
from rest_framework import routers
from .views import ListViewSet

#define la ruta para los modelos, get,post,put,delet,etc
router = routers.DefaultRouter()
router.register(r'',ListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]