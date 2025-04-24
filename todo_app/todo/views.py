from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Task
# Create your views here.

def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/login')
    return render(request, 'sign.html')