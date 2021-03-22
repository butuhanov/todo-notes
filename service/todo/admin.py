from django.contrib import admin
from .models.project import Project
from .models.todo import Todo

admin.site.register(Project)
admin.site.register(Todo)
