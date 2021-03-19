import io

from rest_framework import serializers


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


class AuthorSerializer(serializers.Serializer):
    # AuthorSerializer содержит простые типы полей.
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    # В метод create передаётся validated_data — словарь валидных данных, а возвращается объект Author.
    def create(self, validated_data):
        return Author(**validated_data)

    # В метод update тоже передаётся validated_data, и вместе с ним instance — объект, который мы хотим изменить.
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance

    # Как и в Django Forms, в Serializers можно добавить дополнительную валидацию по одному или нескольким полям.
    #  Для добавления валидации по некоторому полю в serializer включается
    #  метод validate_<имя поля> (validate_birthday_year).
    #  Чтобы применить это к нескольким полям — метод validate.
    def validate_birthday_year(self, value):
        if value < 0:
            # Для генерации ошибки используется класс serializers.ValidationError.
            raise serializers.ValidationError('Год рождения не может быть отрицательным')
        return value

    def validate(self, attrs):
        if attrs['name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
            raise serializers.ValidationError('Неверный год рождения Пушкина')
        return attrs


class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    #  в поле author мы указали AuthorSerializer.
    #  Таким образом, после сериализации получим вложенный словарь с данными автора.
    author = AuthorSerializer()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    #  в поле author мы указали AuthorSerializer.
    #  и добавили к нему дополнительный ключ many=True, так как книгу могут написать несколько авторов.
    #  После сериализации получим вложенный список, состоящий из словарей с данными автора.
    authors = AuthorSerializer(many=True)

class ArticleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    #  в поле author мы указали AuthorSerializer.
    #  Таким образом, после сериализации получим вложенный словарь с данными автора.
    author = AuthorSerializer()


class Command(BaseCommand):
    help = 'serializer example'

    def handle(self, *args, **options):

      # Первым делом мы создали serializer для класса Author.
      # Для этого мы наследуемся от класса serializers.Serializer и определяем нужные типы полей.
      # Таким образом, сериализатор может быть привязан к django-модели или нет.
      # сериализатор напоминает уже знакомые нам Django Forms: Form — не связана с моделью, а ModelForm — связана.


      author1 = Author('Грин', 1880)
      serializer = AuthorSerializer(author1)
      print(serializer.data)  # {'name': 'Грин', 'birthday_year': 1880}

      biography = Biography('Текст биографии', author1)
      serializer = BiographySerializer(biography)
      print(
          serializer.data)  # {'text': 'Текст биографии', 'author': OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])}

      article = Article('Некоторая статья', author1)
      serializer = ArticleSerializer(article)
      print(
          serializer.data)  # {'name': 'Некоторая статья', 'author': OrderedDict([('name', 'Грин'), ('birthday_year', 1880)])}

      author2 = Author('Пушкин', 1799)
      book = Book('Некоторая книга', [author1,
                                      author2])  # {'name': 'Некоторая книга', 'authors': [OrderedDict([('name', 'Грин'), ('birthday_year', 1880)]), OrderedDict([('name', 'Пушкин'), ('birthday_year', 1799)])]}

      serializer = BookSerializer(book)
      print(serializer.data)


      # При передаче только словаря данных и вызова метода save будет вызван метод create.
      data = {'name': 'Грин', 'birthday_year': 1880}
      serializer = AuthorSerializer(data=data)
      # Перед каждым сохранением объекта нужно вызывать метод is_valid serializer-а
      # для проверки данных, иначе возникнет ошибка.
      serializer.is_valid()
      author = serializer.save()
      print(serializer.data)

      # При передаче объекта author и словаря данных объект изменится и будет вызван метод update.
      data = {'name': 'Александр', 'birthday_year': 1880}
      serializer = AuthorSerializer(author, data=data)
      serializer.is_valid()
      author = serializer.save()
      print(serializer.data)

      # data = {'name': 'Грин', 'birthday_year': 'abc'}
      # serializer = AuthorSerializer(data=data)
      # print(serializer.is_valid())  # False
      # print(
      #     serializer.errors)

      # Пример проверки валидации
      data = {'name': 'Пушкин', 'birthday_year': 1799}
      serializer = AuthorSerializer(author, data=data)
      serializer.is_valid()
      author = serializer.save()
      print(serializer.data)

      data = {'name': 'Пушкин', 'birthday_year': 1800}
      serializer = AuthorSerializer(author, data=data)
      serializer.is_valid()
      print('ошибки:', serializer.errors)
      # author = serializer.save()

      data = {'name': 'Пушкин', 'birthday_year': -100}
      serializer = AuthorSerializer(author, data=data)
      serializer.is_valid()
      print('ошибки:', serializer.errors)
      # author = serializer.save()


      # data = {'name': 'Александр', 'birthday_year': -10}
      # serializer = AuthorSerializer(author, data=data)
      # serializer.is_valid()
      # author = serializer.save()

      print(
          serializer.errors)  # {'birthday_year': [ErrorDetail(string='A valid integer is required.', code='invalid')]}

      # При невалидных данных возникнет ошибка, если вызвать метод is_valid и
      # передать в него параметр raise_exception=True.
      serializer.is_valid(raise_exception=True)


      # По умолчанию для обновления объекта нужно передать все поля сериализатора (name и birthday_year).
      # Если же мы хотим передать только несколько полей, а остальные оставить как есть,
      # то нужно использовать параметр partial=True.


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
