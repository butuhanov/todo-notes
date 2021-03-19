from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Biography, Article, Book


# class AuthorModelSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = Author  # сериализатор на основании неё будет создавать JSON-представление
#        fields = '__all__' # какие поля из модели будут отображаться в json. __all__ означает все поля.

#  ModelSerializer наследуется от Serializer.
# Теперь для создания всех serializers используем serializers.ModelSerializer.
class AuthorSerializer(serializers.ModelSerializer):
   #  Минимальные настройки для ModelSerializer:
   # модель с которой связан serializer;
   # набор полей для отображения.
   class Meta:
       model = Author
       fields = '__all__'  # отображать все поля модели, включая вложенные.
       # fields = ['text', 'author']  # указать список полей через запятую
       # exclude = ['name']  # отображать все поля, кроме исключённых


class BiographySerializer(serializers.ModelSerializer):
    # При настройке сериализации вложенных полей можно использовать следующие возможности:
    # указать serializer вложенной модели;
    # указать специальный тип сериализатора;
    # ничего не указывать.

    # Модель Biography связана с Author.
    # Но при настройке сериализатора мы ничего не указали.
    # В этом случае при сериализации будет взят id модели Author.
   class Meta:
       model = Biography
       fields = ['text', 'author']

class ArticleSerializer(serializers.ModelSerializer):
    # Модель Article тоже связана с Author, а в сериализаторе мы указали author = AuthorSerializer().
   # В этом случае за отображение будет отвечать AuthorSerializer(), и на выходе появится вложенный словарь.
   author = AuthorSerializer()

   class Meta:
       model = Article
       exclude = ['name']

class BookSerializer(serializers.ModelSerializer):
    # Модель Book тоже связана с Author, причём авторов может быть много.
    # В этом случае указан специальный тип поля serializers.StringRelatedField(many=True).
    # Он говорит, что автор будет представлен методом __str__ в модели Author,
    # а ключ many=True позволяет выводить несколько авторов.
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'

author1 = Author.objects.create(name='Грин', birthday_year=1880)
serializer = AuthorSerializer(author1)
print(serializer.data)  # {'id': 17, 'name': 'Грин', 'birthday_year': 1880}

biography = Biography.objects.create(text='Некоторая биография', author=author1)
serializer = BiographySerializer(biography)
print(serializer.data)  # {'text': 'Некоторая биография', 'author': 17}

article = Article.objects.create(name='Некоторая статья', author=author1)
serializer = ArticleSerializer(article)
print(serializer.data)  # {'id': 8, 'author': OrderedDict([('id', 17), ('name', 'Грин'), ('birthday_year', 1880)])}

author2 = Author.objects.create(name='Пушкин', birthday_year=1799)
book = Book.objects.create(name='Некоторая книга')
book.authors.add(author1)
book.authors.add(author2)
book.save()
serializer = BookSerializer(book)
print(serializer.data)  # {'id': 9, 'authors': ['Грин', 'Пушкин'], 'name': 'Некоторая книга'}
