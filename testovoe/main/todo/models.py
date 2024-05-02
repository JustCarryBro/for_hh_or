import datetime
from django.utils import timezone

from django.db import models

class TodoListItem(models.Model):

    title = models.TextField()
    desription = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)




    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.title

