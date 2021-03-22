from django.db import models
from uuid import uuid4
from todo.models import Project

class User(models.Model):
   uuid = models.UUIDField(primary_key=True, default=uuid4)
   username = models.CharField(max_length=64)
   firstname = models.CharField(max_length=64)
   lastname = models.CharField(max_length=64)
   email = models.EmailField(max_length=64, unique = True)

   # у одного проекта может быть несколько пользователей, поэтому используем отношение "один ко многим"
   # Одна главная сущность может быть связана с несколькими зависимыми
   # Проект в данном случае будет главной моделью, а модель User - зависимой
   project = models.ForeignKey(Project, on_delete=models.PROTECT)

   # Конструктор типа models.ForeignKey настраивает связь с главной сущностью.
   # Первый параметр указывает, с какой моделью будет создаваться связь - в данном случае это модель Company.
   # Второй параметр - on_delete задает опцию удаления объекта текущей модели
   # при удалении связанного объекта главной модели
   # models.CASCADE: автоматически удаляет строку из зависимой таблицы,
   # если удаляется связанная строка из главной таблицы
   # models.PROTECT: блокирует удаление строки из главной таблицы,
   # если с ней связаны какие-либо строки из зависимой таблицы