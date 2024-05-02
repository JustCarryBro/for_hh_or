from django.contrib import admin
from .models import TodoListItem

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','desription','date')
    list_display_links = ('id','title')





admin.site.register(TodoListItem)