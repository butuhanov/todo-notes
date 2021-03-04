from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = User  # сериализатор на основании неё будет создавать JSON-представление
       fields = 'username, firstname, lastname, email' # какие поля из модели будут отображаться в json.
