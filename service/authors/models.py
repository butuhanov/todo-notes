from django.db import models
from uuid import uuid4

class Author(models.Model):
   uuid = models.UUIDField(primary_key=True, default=uuid4)
   first_name = models.CharField(max_length=64)
   last_name = models.CharField(max_length=64)
   birthday_year = models.PositiveIntegerField()

# Метод str-модели Author возвращает имя автора.
   def __str__(self):
       return self.last_name


class Biography(models.Model):
   text = models.TextField()
   author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
   name = models.CharField(max_length=32)
   authors = models.ManyToManyField(Author)

class Article(models.Model):
   # Модель описывает статью, у которой есть название, написавший её пользователь, текст и дата создания.
   name = models.CharField(max_length=32)
   author = models.ForeignKey(Author, models.PROTECT)
   text = models.TextField()

   create = models.DateTimeField()

   def __str__(self):
       return self.name
