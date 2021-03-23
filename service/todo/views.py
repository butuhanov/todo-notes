from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from todo.models.todo import Todo
from todo.models.project import Project
from .serializers import TodoSerializer, ProjectSerializer



from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 10

class TodoModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

   queryset = Todo.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   serializer_class = TodoSerializer # serializer_class определяет тот Serializer, который мы будем использовать.

from .filters import ProjectFilter
class ProjectModelViewSet(ModelViewSet):  # Мы используем наследование от ModelViewSet.


# Это означает, что набор views связан с моделью и будет работать с её данными.

    queryset = Project.objects.all()  # queryset указывает, какие данные мы будем выводить в списке.
    serializer_class = ProjectSerializer  # serializer_class определяет тот Serializer, который мы будем использовать.
    filter_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination

