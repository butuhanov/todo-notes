# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from authors.views import AuthorModelViewSet
#
# # Создаём объект класса DefaultRouter и связываем AuthorModelViewSet с адресом authors.
# router = DefaultRouter()
# router.register('authors', AuthorModelViewSet)
#
# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('api-auth/', include('rest_framework.urls')),
#    path('api/', include(router.urls)),  # Подключаем адреса (urls), которые формирует роутер, к нашему проекту.
# ]