from django.forms import ModelForm,TextInput
from .models import TodoListItem

class TodoListForm(ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['title','desription']
        widgets = {'title': TextInput(attrs={'class':'testovoe'}),
                   'desription': TextInput(attrs={'class':'testovoe'})}