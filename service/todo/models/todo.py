from django.db import models
from uuid import uuid4

from users.models import User
from todo.models.project import Project

class Todo(models.Model):
   #  Это заметка. У To Do есть проект, в котором сделана заметка,
   #   текст заметки, дата создания и обновления, пользователь, создавший заметку.
   # Содержится и признак — активно TO DO или закрыто.

   # Для связи с проектом, используем отношение один к одному, которое предполагает,
   # что одна строка из одной таблицы может быть связана только с одной сущностью из другой таблицы.
   # Третий параметр primary_key = True указывает, что внешний ключ (через который идет связь с главной моделью)
   # в то же время будет выступать и в качестве первичного ключа.
   # И соответственно создавать отдельное поле для первичного ключа не надо.

   project = models.ForeignKey(Project, on_delete = models.CASCADE) # у проекта может быть много заметок to do

   #   текст заметки
   # TextField(): хранит строку неопределенной длины
   text = models.TextField()

   # дата создания
   created = models.DateTimeField(auto_now=False, auto_now_add=True)
   # дата обновления
   updated = models.DateTimeField(auto_now=True, auto_now_add=False)
   # пользователь, создавший заметку
   creator = models.ForeignKey(User, on_delete=models.PROTECT) # пользователь может создать много заметок
