from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
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
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('register')   
                else:
                  user = User.objects.create_user(username=username, password=password, email=email, 
                  first_name=first_name, last_name=last_name)
                  #login after register
                  #auth.login request user
                  #message success
                  #return redirect
                  user.save() 
                  messages.success(request, 'You are register and can login')
                  return redirect('login')
                  
        else:
            messages.error(request, 'An unexpected error occured')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'user password not incorrect')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    user_contact = Contact.objects.order_by('contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contact
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are logout')
        return redirect('index') 