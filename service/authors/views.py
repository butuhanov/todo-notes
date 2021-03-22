from rest_framework.viewsets import ModelViewSet

from rest_framework.renderers import JSONRenderer
from .models import Article
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer, ArticleSerializer

from rest_framework.decorators import api_view, renderer_classes



class AuthorModelViewSet(ModelViewSet): # Мы используем наследование от ModelViewSet.
                                        # Это означает, что набор views связан с моделью и будет работать с её данными.

   queryset = Author.objects.all() # queryset указывает, какие данные мы будем выводить в списке.
   serializer_class = AuthorSerializer # serializer_class определяет тот Serializer, который мы будем использовать.


from rest_framework.views import APIView

class ArticleAPIVIew(APIView):
    # Рассмотрим для начала класс APIView.
    # Это базовый класс для Views в DRF.
    # Он может быть связан с другими частями DRF (например, Renderers)
    # и позволяет полностью самостоятельно написать код обработки того или иного запроса.

    # Свойство renderer_classes позволяет указать список Renderers.
   renderer_classes = [JSONRenderer]

    # Метод get отвечает за get-запрос.
    # Мы получаем все статьи, с помощью ArticleSerializer
    # преобразуем выборку в простые типы данных и возвращаем объект Response.
    # Важно! Для ответа используется объект класса Respose из DRF, а не из django.
   def get(self, request, format=None):
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return Response(serializer.data)

# DRF позволяет создавать Views не только на классах, но и на функциях.
# В примере ниже мы создали View с такими же опциями, как и в предыдущем, но использовали функцию.
# Для указания доступных запросов используется декоратор @api_view, а для Renderers — декоратор renderer_classes.
# Приминение:
# Базовые View удобно использовать для решения нестандартных задач, которые требуют написания множества уникального кода.
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
   articles = Article.objects.all()
   serializer = ArticleSerializer(articles, many=True)
   return Response(serializer.data)

# Следующим уровнем можно считать GenericAPIVIew.
# Этот класс наследуется от APIView и содержит в себе наиболее общие свойства и методы,
# такие как queryset, get_queryset и serializer_class.
# Таким образом, подразумевается, что мы уже работаем с некоторым набором данных и классом для их сериализации.
# При добавлении некоторых классов примесей (mixins) и использования GenericAPIView
# можно получить конкретные классы для той или иной задачи (REST-запроса).
# Полный список классов можно найти в официальной документации
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes


# Concrete Views
from rest_framework.generics import CreateAPIView

class ArticleCreateAPIView(CreateAPIView):
    # Предоставляет метод post. Для создания модели достаточно указать queryset и serializer_class

    renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

# ListAPIView
from rest_framework.generics import ListAPIView

# Предоставляет метод get и выводит список данных из выборки queryset.
class ArticleListAPIView(ListAPIView):
   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

# RetrieveAPIView
from rest_framework.generics import RetrieveAPIView


class ArticleRetrieveAPIView(RetrieveAPIView):
    # Выдаёт метод get и выводит данные об одном объекте из выборки queryset.
    # Для указания адреса требуется параметр pk, чтобы определить id элемента.

   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
    # Пример использования: в blog/urls.py
    # path('generic/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view())

# DestroyAPIView
from rest_framework.generics import DestroyAPIView


class ArticleDestroyAPIView(DestroyAPIView):
    # Предоставляет метод delete и удаляет один объект из выборки. В адресе также требуется указать pk объекта.
   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

# UpdateAPIVIew
from rest_framework.generics import UpdateAPIView


class ArticleUpdateAPIView(UpdateAPIView):
    # Выдаёт методы put и patch для изменения объекта из выборки queryset. Требует pk в url-адресе.
   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer