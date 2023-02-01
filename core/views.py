from django.shortcuts import render, redirect

from .models import Todo
from .form import TodoForm

# Create your views here.

def TodosList(request):
    todos = Todo.objects.all
    return render(request, 'core/index.html', {'todos':todos})

def TodoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'core/detail.html',{'todo':todo})

def TodoCreate(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'core/create.html', {'form':form})

def TodoDelete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')

def TodoDone(request,pk):
    todo = Todo.objects.get(id=pk)
    if todo.done == False:
        todo.done = True
    else:
        todo.done = False
    todo.save()
    return redirect('index')

def TodoUpdate(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'core/create.html',{'form':form})