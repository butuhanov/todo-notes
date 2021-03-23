from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
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
    permission_classes = [AllowAny]

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

# ViewSets
# ViewSets (наборы представлений) позволяют объединять несколько представлений в один набор.
# Причём можно или описать нужные методы для обработки запросов самостоятельно,
# или использовать ModelViewSet для создания набора на основе конкретной модели.
# Можете также собрать ViewSet из нескольких Views. Рассмотрим каждую возможность.

# Класс ViewSet в DRF позволяет на его основе создавать набор данных
# и прописывать важные методы для обработки разных типов запросов.

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, get_object_or_404

class ArticleViewSet(viewsets.ViewSet):
   renderer_classes = [JSONRenderer]

   # В этом примере определены методы list и retrieve.
   # Они соответствуют get-запросам для получения набора данных и информации об одном объекте.
   # Это похоже на работу с APIView,
   # но в нашем случае в одном ViewSet можно описать обработку сразу нескольких REST-запросов.
   def list(self, request):
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return Response(serializer.data)

   def retrieve(self, request, pk=None):
       article = get_object_or_404(Article, pk=pk)
       serializer = ArticleSerializer(article)
       return Response(serializer.data)

# Дополнительные действия
# Часто требуется добавить некоторые дополнительные действия в наше API, например, изменение пароля пользователя.
# Класс ViewSet позволяет это сделать.
# Рассмотрим пример, в котором нужно по определённому адресу выдавать не всю информацию о статье (модели Article),
# а только её текст.
# Viewset в этом случае может выглядеть так:

from rest_framework.decorators import action

class ArticleViewSet(viewsets.ViewSet):
   renderer_classes = [JSONRenderer]

   # Получаем объект Article и возвращаем пользователю только его текст.
   # Чтобы роутер распознал дополнительное действие, нужен декоратор @action(detail=True, methods=['get']).
   # В нём указываем методы, доступные для этого действия, и detail.
   # Параметр detail показывает, работаем ли мы со всей выборкой или с одним объектом.
   # Для одного объекта в адрес добавляется pk.
   # В urls.py для регистрации в роутере никаких дополнительных действий не требуется.
   # Роутер сам создаст адрес следующего вида: /viewsets/viewset/1/article_text_only/.
   # в этом примере http://127.0.0.1:8000/viewsets/base/1/article_text_only/
   # В этом адресе цифра 1 — это pk статьи Article.
   @action(detail=True, methods=['get'])
   def article_text_only(self, request, pk=None):
       article = get_object_or_404(Article, pk=pk)
       return Response({'article.text': article.text})

   def list(self, request):
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return Response(serializer.data)

   def retrieve(self, request, pk=None):
       article = get_object_or_404(Article, pk=pk)
       serializer = ArticleSerializer(article)
       return Response(serializer.data)

# ModelViewSet
# Мы уже немного работали с ModelViewSet.
# Этот класс основан на GenericViewSet и позволяет быстро построить API для модели данных.
# Это полезно в тех случаях, когда нужны почти все REST API-запросы для конкретной модели.
class ArticleModelViewSet(viewsets.ModelViewSet):
    # Для базового использования достаточно указать queryset и serializer_class.
    # Для настройки можно переопределить любой метод классов ViewSet и ModelViewSet,
    # а также добавить дополнительные действия.
   queryset = Article.objects.all()
   renderer_classes = [JSONRenderer]
   serializer_class = ArticleSerializer

# Custom ViewSet
# Один из наиболее удобных видов Viewset — Viewset, собранный из нескольких примесей (mixins).
# Примеси могут быть взяты из DRF, так и являться своими классами.
# Рассмотрим пример создания такого Viewset.
from rest_framework import mixins

class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # Основа — GenericViewSet.
    # К нему добавляются нужные классы примеси.
    # Таким образом, от того, какие примеси добавлены, будет зависеть доступность запросов REST API.
    # В этом примере добавился CreateModelMixen, ListModelMixin, RetrieveModelMixin.
    # Это означает, что нам будут доступны запросы get и post.
    # Появятся возможности создавать новые записи, просматривать список или одну запись.
    # Далее стандартно указывается queryset и serializer_class.
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # Урлы для этого Viewset генерируются также через Router.
# Применение
# Чаще используются ModelViewSet и Custom Viewset.
# ModelViewSet удобен, когда нужно большинство методов для одной модели данных,
# а Custom Viewset — при необходимости только части методов для API.
# Класс ViewSet используется реже для нестандартных задач и нескольких типов rest-запросов.


# Filtering
# Добавление фильтрации в REST API — стандартная задача.
# Часто требуется вывести данные только для конкретного пользователя,
# либо отфильтровать данные по части имени или дате добавления.
# DRF предоставляет удобные средства для создания фильтров.
# Рассмотрим наиболее актуальные варианты.

# get_queryset
# Views и Viewsets, которые содержат свойство queryset,
# также имеют метод get_queryset для получения выборки данных динамически.
# Если этот метод не переопределился, по умолчанию он возвращает свойство queryset.
# Если переопределим этот метод, сможем пользоваться методом filter у менеджера моделей objects.
# Рассмотрим это на примере:
class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet):
    # В примере используется ModelViewSet.
    # Но это актуально и для других Views и Viewset, у которых есть свойство queryset.
   serializer_class = ArticleSerializer
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   queryset = Article.objects.all()

   def get_queryset(self):
       # После переопределения метода get_queryset берём не все данные, а фильтруем статьи Article по части имени.
       # В нашем случае имя должно содержать слово python.
       return Article.objects.filter(name__contains='python')


# kwargs
# В предыдущем примере ‘python’ содержится в коде.
# Часто мы хотим предоставить пользователю возможность вводить данные для фильтрации.
# Это можно сделать двумя основными способами:
# через параметр в url-адресе;
# через параметры запроса.
# Когда мы используем параметры в url-адресе, то данные фильтра получаем через kwargs запроса.
# Рассмотрим это на примере:
class ArticleKwargsFilterView(ListAPIView):
   serializer_class = ArticleSerializer

   def get_queryset(self):
       # Из self.kwargs берётся по ключу параметр name и затем передаётся в фильтр.
       # Адрес при этом должен содержать строковый параметр name
       name = self.kwargs['name']
       return Article.objects.filter(name__contains=name)

# Параметры запроса
# адрес можно оставить таким, какой создаст Router.
# Сам Viewset в этом случае будет выглядеть следующим образом
# Пример http://127.0.0.1:8000/filters/param/?name=python

class ArticleParamFilterViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

   def get_queryset(self):
       name = self.request.query_params.get('name', '')
       articles = Article.objects.all()
       if name:
           articles = articles.filter(name__contains=name)
       return articles

 # DjangoFilter
# Метод get_queryset позволяет добавить в приложении любые типы фильтров.
# Однако при частом использовании будет много одинакового кода по получению параметров из адреса и передачу их в фильтр.
# Часто нужно обрабатывать ситуацию, когда параметр может быть или отсутствовать.
# Для некоторых фильтров, например, фильтр по дате, не придётся получать дату как строку и приводить её в нужный вид.
# Библиотека django-filter и возможность её быстрой интеграции в DRF позволяют
# быстро добавлять фильтры из нескольких полей разного типа.
# Для работы с django-filter можно обратиться к её официальной документации
# https://django-filter.readthedocs.io/en/stable/.
# Важно смотреть раздел интеграции с DRF, https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
# так как подключение фильтров к DRF немного отличается от подключения фильтров к Django.

# Рассмотрим примеры создания и настройки фильтров.
# В большинстве случаев нам нужно только указать поля, по которым хотим добавить фильтрацию.

class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    # При добавлении во VIew или Viewset свойства filterset_fields с указанием списка полей получаем готовый фильтр.
    # В браузере при этом появится кнопка «Фильтр», а сами данные будут передаваться как параметры запроса.
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   filterset_fields = ['name', 'user']

# Если, кроме указания полей, необходимо настроить их отображение и тип, то сначала создаём фильтр в файле filters.py
# Важно! Фильтры рекомендуется создавать в отдельном файле filters.py внутри приложения.

# После того как создали фильтр, импортируем его в файл,
# где находиться Viewset и указываем нужный фильтр внутри VIewset:
from .filters import ArticleFilter


class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   filterset_class = ArticleFilter

# LimitOffsetPagination
# Этот вид постраничного вывода более гибкий, чем PageNumberPagination.
# Обычно используется для API, в которых клиент может сам решать. Например, сколько данных он
# хочет получить, и с какой точки отсчитывать это количество.

from rest_framework.pagination import LimitOffsetPagination


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    # Для начала мы создали свой класс на основе LimitOffsetPagination.
    # default_limit — показывает сколько записей по умолчанию будет выводиться,
    # если этот параметр не будет передан в запросе.
   default_limit = 2


class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   # Затем конкретному Viewset указываем класс для постраничного вывода.
   # Этот класс переопределяет настройку по умолчанию.
   # Запрос будет выглядеть так http://127.0.0.1:8000/pagination/limitoffset/?limit=2&offset=2
   pagination_class = ArticleLimitOffsetPagination