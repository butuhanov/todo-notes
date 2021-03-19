from django.db import models
from uuid import uuid4

from users.models import User

# Это проект, для которого записаны TO DO.
# У него есть название, может быть ссылка на репозиторий и набор пользователей, которые работают с этим проектом.
# Создать модель, выбрать подходящие типы полей и связей с другими моделями.
class Project(models.Model):
   uuid = models.UUIDField(primary_key=True, default=uuid4)
   name = models.CharField(max_length=64) # название проекта
   repo_link = models.URLField() # ссылка на репозиторий

   # у одного проекта может быть несколько пользователей, поэтому используем отношение "один ко многим"
   # Одна главная сущность может быть связана с несколькими зависимыми
   # models.CASCADE: автоматически удаляет строку из зависимой таблицы,
   # если удаляется связанная строка из главной таблицы
   # models.PROTECT: блокирует удаление строки из главной таблицы,
   # если с ней связаны какие-либо строки из зависимой таблицы
   users = models.ForeignKey(User, on_delete=models.PROTECT)

#  Это заметка. У To Do есть проект, в котором сделана заметка,
#   текст заметки, дата создания и обновления, пользователь, создавший заметку.
# Содержится и признак — активно TO DO или закрыто.
class Todo(models.Model):

   # Для связи с проектом, используем отношение один к одному, которое предполагает,
   # что одна строка из одной таблицы может быть связана только с одной сущностью из другой таблицы.
   # Третий параметр primary_key = True указывает, что внешний ключ (через который идет связь с главной моделью)
   # в то же время будет выступать и в качестве первичного ключа.
   # И соответственно создавать отдельное поле для первичного ключа не надо.
   project = models.OneToOneField(Project, on_delete = models.PROTECT, primary_key = True)

   #   текст заметки
   # TextField(): хранит строку неопределенной длины
   name = models.TextField()

   # дата создания
   created = models.DateTimeField(auto_now=False, auto_now_add=True)
   # дата обновления
   updated = models.DateTimeField(auto_now=True, auto_now_add=False)
   # пользователь, создавший заметку
   user = models.OneToOneField(User, on_delete=models.PROTECT)
