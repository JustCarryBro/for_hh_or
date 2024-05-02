from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import TodoListItem
from .forms import TodoListForm

class NewModelUpdate(UpdateView):
    model = TodoListItem
    template_name = 'update.html'
    form_class = TodoListForm


def index(request):
    todo = TodoListItem.objects.all()
    if request.method == 'POST':
        new_todo = TodoListItem(
            title = request.POST['title'],
            desription = request.POST['desription']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'text': todo})

def delete(request, pk):
    todo = TodoListItem.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def test(request):
    return HttpResponse("<h1>ТЕСТОВОЕ<h1>")

