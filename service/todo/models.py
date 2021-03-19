from django.db import models
from uuid import uuid4

from service.users.models import User


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
