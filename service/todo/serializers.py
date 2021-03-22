from rest_framework import serializers
from todo.models.todo import Todo
from todo.models.project import Project
from users.serializers import UserModelSerializer

class TodoSerializer(serializers.ModelSerializer):
    # Модель To do связана с User, а в сериализаторе мы указали user = UserModelSerializer().
   # В этом случае за отображение будет отвечать UserModelSerializer(), и на выходе появится вложенный словарь.
   user = UserModelSerializer()
   class Meta:
       model = Todo
       fields = 'project', 'name', 'created', 'updated', 'user'

class ProjectSerializer(serializers.ModelSerializer):
   # Модель Project связана с User и To do
   project = TodoSerializer()
   user = UserModelSerializer()

   class Meta:
       model = Project
       fields = '__all__'  # отображать все поля модели, включая вложенные.

