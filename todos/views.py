from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from accounts.models import Profile

from django.utils import timezone

# Create your views here.
@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['point_value']:
            todo = Todo()
            todo.title = request.POST['title']
            todo.pub_date = timezone.now()
            todo.author = request.user
            todo.point_value = int(request.POST['point_value'])
            todo.completed = False
            todo.save()
        return redirect('todos:home')
    else:
        todos = Todo.objects.order_by('-pub_date')
        return render(request, 'todos/index.html', {'todos': todos})

@login_required(login_url='/accounts/login/')
def home(request):
    todos = Todo.objects.filter(completed=False).filter(author=request.user).order_by('-pub_date')
    completed_todos = Todo.objects.filter(completed=True).filter(author=request.user).order_by('-pub_date')

    return render(request, 'todos/index.html', {'todos': todos, 'completed_todos': completed_todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    return render(request, 'todos/todo_detail.html', {'todo': todo})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.pub_date = timezone.now()
            todo.completed = todo.completed
            todo.save()
            return redirect('todos:home')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_edit.html', {'form': form})

def mark_complete(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = True
        todo.save()

        # Add exp points to user profile
        profile = Profile.objects.get(user=request.user)
        profile.gain_exp(todo.point_value)
        profile.save()

        return redirect('todos:home')

def unmark_complete(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = False
        todo.save()
        return redirect('todos:home')

def delete_todo(request, pk):
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('todos:home')

def clear_completed(request):
    completed_todos = Todo.objects.filter(completed=True).filter(author=request.user)
    for completed in completed_todos:
        completed.delete()

    return redirect('todos:home')
