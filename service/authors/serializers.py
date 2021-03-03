from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = Author  # сериализатор на основании неё будет создавать JSON-представление
       fields = '__all__' # какие поля из модели будут отображаться в json. __all__ означает все поля.