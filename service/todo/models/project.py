from django.db import models
from uuid import uuid4

from users.models import User


class Project(models.Model):
   # Это проект, для которого записаны TO DO.
   # У него есть название, может быть ссылка на репозиторий и набор пользователей, которые работают с этим проектом.
   # Создать модель, выбрать подходящие типы полей и связей с другими моделями.
   uuid = models.UUIDField(primary_key=True, default=uuid4)
   name = models.CharField(max_length=64) # название проекта
   repo_link = models.URLField(blank=True) # ссылка на репозиторий
   users = models.ManyToManyField(User)

   # у одного проекта может быть несколько пользователей, поэтому используем отношение "один ко многим"
   # Одна главная сущность может быть связана с несколькими зависимыми
   # Проект в данном случае будет главной моделью, а модель User - зависимой
   # Поэтому настраивать надо в модели User

   def _str_(selfself):
      return self.name
