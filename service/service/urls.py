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
from users.views import UserModelViewSet
from todo.views import TodoModelViewSet, ProjectModelViewSet


# Создаём объект класса DefaultRouter и связываем AuthorModelViewSet с адресом authors.
from users import views

from users.views import UserCustomViewSet

router = DefaultRouter()
# router.register('users', UserModelViewSet)
router.register('todo', TodoModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('user', UserModelViewSet, basename='user')

# При регистрации ViewSet указываем точку входа, сам ViewSet и его имя.
# Затем подключаем urls роутера в urlpatterns.

router.register('userview', UserCustomViewSet)



# router.register('user', views.UserModelViewSet, basename='user')


urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),  # Подключаем адреса (urls), которые формирует роутер, к нашему проекту.
   path('api-token-auth/', obtain_auth_token),
]