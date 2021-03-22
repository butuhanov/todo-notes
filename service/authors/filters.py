from django_filters import rest_framework as filters
from .models import Article


class ArticleFilter(filters.FilterSet):
    # указываем модель, для которой создаётся фильтр, список доступных полей, настройку для каждого поля.
    # name = filters.CharFilter(lookup_expr='contains') в этом примере мы указали,
    # что к фильтру в поле name нужно добавить contains для поиска по части имени, а не по полному совпадению.
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Article
       fields = ['name']
