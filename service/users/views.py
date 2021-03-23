from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer

from .filters import UserFilter

class UserModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

   queryset = User.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   serializer_class = UserModelSerializer # serializer_class определяет тот Serializer, который мы будем использовать.
   # filterset_fields = ['username']
   filter_class = UserFilter
