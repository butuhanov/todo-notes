from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer

from .filters import UserFilter

class UserModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

    renderer_classes = [JSONRenderer]

    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, username=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=['update'])
    def updateuser(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        return Response({'user.lastname': user.lastname})



   # queryset = User.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   # serializer_class = UserModelSerializer # serializer_class определяет тот Serializer, который мы будем использовать.
   # # filterset_fields = ['username']
   # filter_class = UserFilter
