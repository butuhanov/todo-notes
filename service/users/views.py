from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer

import logging

service_log = logging.getLogger('service_log')

from .filters import UserFilter

class UserModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

    queryset = User.objects.all()  # queryset указывает, какие данные мы будем выводить в списке.
    serializer_class = UserModelSerializer  # serializer_class определяет тот Serializer, который мы будем использовать.

    #
    # renderer_classes = [JSONRenderer]
    #
    # def list(self, request):
    #     users = User.objects.all()
    #     serializer = UserModelSerializer(users, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     user = get_object_or_404(User, username=pk)
    #     serializer = UserModelSerializer(user)
    #     return Response(serializer.data)
    #
    # @action(detail=True, methods=['update'])
    # def updateuser(self, request, pk=None):
    #     user = get_object_or_404(User, pk=pk)
    #     return Response({'user.lastname': user.lastname})



   # queryset = User.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   # serializer_class = UserModelSerializer # serializer_class определяет тот Serializer, который мы будем использовать.
   # # filterset_fields = ['username']
   # filter_class = UserFilter


# Чаще используются ModelViewSet и Custom Viewset.
# ModelViewSet удобен, когда нужно большинство методов для одной модели данных,
# а Custom Viewset — при необходимости только части методов для API.
# Класс ViewSet используется реже для нестандартных задач и нескольких типов rest-запросов.

# Пример Custom ViewSet
from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class UserCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # С таким набором миксинов будут доступны GET и POST, также можно добавить destroy, update

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    filterset_fields = ['email', 'lastname']

    # пример extra action
    @action(detail=True, methods=['get'])
    def user_lastname_only(self, request, pk=None):
        # http://127.0.0.1:8000/api/userview/uuid/user_lastname_only/
        user = get_object_or_404(User, pk=pk)
        return Response({'user.lastname': user.lastname})


# Пример ViewSet
class UserViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]


    def get_queryset(self):
        return User.objects.filter(email__contains='user2')  # пример использования фильтра

    def list(self,request): # весь набор данных
        # users = User.objects.all()
        serializer = UserModelSerializer(self.get_queryset(), many=True, context={'request': request})
        # service_log.info(f'{dir(request)}')
        service_log.info(f'data - {request.data}, POST - {request.POST}')
        return Response(serializer.data)


    def retreive(self,request): # доступ к request позволяет настроить логирование
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return(serializer.data)

# Если нужна своя логика, можно использовать APIView, но в команде могут использоваться и другие способы
# class UserAPIView(APIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def get_queryset(self):
#         return User.objects.filter(email__contains='123')  # пример использования фильтра
#
#     def get(self, request, format=None):
#         # users = User.objects.all()
#         users = User.objects.filter(email__contains='123')
#         serializer = UserModelSerializer(users, many=True, context={'request': request})
#
#         # serializer = UserModelSerializer(users, many=True)
#         service_log.info(f'data - {request.data}, POST - {request.POST}')
#         return(serializer.data)
#     #
#     # @classmethod
#     # def get_extra_actions(cls):
#     #     return []

# Пример получения параметров из URL
class UserKwargsFilterView(ListAPIView):
    serializer_class = UserModelSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return User.objects.filter(email__contains=email)

