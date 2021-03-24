"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, ArticleAPIVIew, BookModelViewSet
from authors import views

# Создаём объект класса DefaultRouter и связываем AuthorModelViewSet с адресом authors.


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', views.BookModelViewSet, basename='books')

router.register('base', views.ArticleViewSet, basename='article')
# указываем точку входа, сам ViewSet и его имя. Затем подключаем urls роутера в urlpatterns.
# Важно! При использовании ViewSet укажите basename при регистрации в роутере.
# Потому что наш ViewSet не связан с моделью данных и какой-либо выборкой.
# Нет признака, по которому DRF сам сможет создать название url-адреса.

# Параметры запроса
# Если мы используем параметры запроса для передачи параметров, то специальный адрес делать не нужно
filter_router = DefaultRouter()
filter_router.register('param', views.ArticleParamFilterViewSet)
# также надо добавить путь в urlpatterns

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),  # Подключаем адреса (urls), которые формирует роутер, к нашему проекту.
   path('views/api-view/', views.ArticleAPIVIew.as_view()),
   path('viewsets/', include(router.urls)),
   path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),
   path('filters/', include(filter_router.urls)), # Параметры запроса
   path('api-token-auth/', obtain_auth_token),
]