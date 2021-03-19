import io

from rest_framework import serializers

# from python_models import Author

from django.core.management.base import BaseCommand


class Author:

   def __init__(self, name, birthday_year):
       self.name = name
       self.birthday_year = birthday_year

   def __str__(self):
       return self.name


class Biography:

   def __init__(self, text, author):
       self.author = author
       self.text = text


class Book:

   def __init__(self, name, authors):
       self.name = name
       self.authors = authors


class Article:

   def __init__(self, name, author):
       self.name = name
       self.author = author


class Command(BaseCommand):
    help = 'serializer example'

    def handle(self, *args, **options):

      # Первым делом мы создали serializer для класса Author.
      # Для этого мы наследуемся от класса serializers.Serializer и определяем нужные типы полей.
      # Таким образом, сериализатор может быть привязан к django-модели или нет.
      # сериализатор напоминает уже знакомые нам Django Forms: Form — не связана с моделью, а ModelForm — связана.


      class AuthorSerializer(serializers.Serializer):
         name = serializers.CharField(max_length=128)
         birthday_year = serializers.IntegerField()

      # Далее, если у нас есть объект класса Author, можем передать его в AuthorSerializer и создать объект serializer.

      author = Author('Грин', 1880)
      serializer = AuthorSerializer(author)
      print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}
      # serializer.data — это представление объекта в виде словаря python, который содержит простые типы, доступные в python.
      print(type(serializer.data))  # <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
      # Если проверить type(serializer.data), то увидим специальный тип DRF.
      # Он, в свою очередь, возвращает словарь.
      # Можно опустить этот момент и говорить, что serializer превращает сложный объект в словарь python,
      # содержащий простые типы данных.

      from rest_framework.renderers import JSONRenderer
      renderer = JSONRenderer()
      json_bytes = renderer.render(serializer.data)
      print(json_bytes)  # b'{"name":"\xd0\x93\xd1\x80\xd0\xb8\xd0\xbd","birthday_year":1880}'
      print(type(json_bytes))  # <class 'bytes'>

      # После того как serializer вернул словарь, нам нужно преобразовать его в независимый от языка python формат.
      # Для этого используется Renderer. Можно применить разные Renderers, например, JSONRenderer.
      # Он преобразует данные в формат json.
      # После создания объекта JSONRenderer() в метод render мы передаём словарь данных и получаем на выходе набор байт,
      # содержащий json.
      # При проверке типа результата type(json_bytes) появятся bytes.
      # Внимание! Строго говоря, формат JSON представляет собой текст, а не байты.
      # Приведение в байты сделано для удобства работы самого DRF.
      # Как и в случае с сериализатором, который возвращает rest_framework.utils.serializer_helpers.ReturnDict вместо dict.
      # Концептуально можно говорить, что Render преобразует python-словарь в json.

      from rest_framework.parsers import JSONParser
      stream = io.BytesIO(json_bytes)
      data = JSONParser().parse(stream)
      print(data)  # {'name': 'Грин', 'birthday_year': 1880}
      print(type(data))  # <class 'dict'>

      # Для обратного преобразования из байт, которые содержат json, используется Parser.
      # Парсер принимает в себя специальный тип <class '_io.BytesIO'>, а на выходе возвращает словарь dict с данными.
      # На вход мы подаём данные в виде словаря python и проверяем их на валидность.
      # Если они валидны, на их основании можно восстановить объект Author.
      serializer = AuthorSerializer(data=data)
      print(serializer.is_valid())  # True
      print(serializer.validated_data)  # OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])
      print(type(serializer.validated_data))  # <class 'collections.OrderedDict'>
