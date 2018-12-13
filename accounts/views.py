from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        #messages.error(request, "test for site")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            #messages.error(request, "555555555555555")
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect('register')
            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is taken")
                    return redirect('register')   
                else:
                    messages.error(request, "555555555555")
        else:
            messages.error(request, "password don't match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #
        return
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('index') 