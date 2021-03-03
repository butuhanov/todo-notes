from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

   queryset = Author.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   serializer_class = AuthorModelSerializer # serializer_class определяет тот Serializer, который мы будем использовать.
