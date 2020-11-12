from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
        #Get form values
        
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        #Check if user have same password
        if password == password2:
            #Check username available
            if User.objects.filter(username= username).exists():
                messages.error(request, 'That username is already exists')
                return redirect('register')
            else:
                if User.objects.filter(email= email).exists():
                    messages.error(request, 'That email is already taken')
                    return redirect('register')
                else:
                    user= User.objects.create_user(username= username, first_name= first_name, last_name= last_name, email=email, password=password)
                    #Login after user register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'You are now Register')
                    return redirect('login')

            
        else:
            messages.error(request, "Passwords are not matched ")
            return redirect('register')
    else:
        
     return render(request, 'accounts/register.html')

def login(request):
    if request.method=='POST':
        #Login User
        return
    else:
        
     return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
