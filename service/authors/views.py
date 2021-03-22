from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
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
