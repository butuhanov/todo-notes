from django.contrib import admin
from .models import Author, Article, Book, Biography
# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Biography)
