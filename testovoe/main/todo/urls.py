from django.urls import path
from .views import index,delete,NewModelUpdate


from rest_framework.routers import DefaultRouter
from .api import TodoViewSet

routers = DefaultRouter()
routers.register(r'api/todo',TodoViewSet, basename='todo')


urlpatterns = [
    path('', index, name='index'),
    path('delete/<str:pk>', delete, name='delete'),
    path('update/<int:pk>',NewModelUpdate.as_view(),name='update')
]
urlpatterns += routers.urls