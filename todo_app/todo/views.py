from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Task
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def sign_up_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/login')
    return render(request, 'sign.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo_page')
        else:
            return redirect('login')

    return render(request, 'login.html')
@login_required(login_url='/login')
def todo_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        task = Task(title=title, user=request.user)
        task.save()

        all_tasks = Task.objects.filter(user=request.user).order_by('date')

        return redirect('/todo_page', {'all_tasks': all_tasks})

    all_tasks = Task.objects.filter(user=request.user).order_by('date')
    return render(request, 'todo.html', {'all_tasks': all_tasks})

@login_required(login_url='/login')
def edit_todo_view(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        task = Task.objects.get(id=id)
        task.title = title
        task.save()

        return redirect('/todo_page')

    task = Task.objects.get(id=id)
    return render(request, 'edit_todo.html', {'task': task})

@login_required(login_url='/login')
def delete_todo_view(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect('/todo_page')

def signout_view(request):
    logout(request)
    return redirect('home')

