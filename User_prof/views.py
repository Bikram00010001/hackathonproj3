from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if email and username and password:
            try:
                user = Profile.objects.create_user(email=email, username=username, password=password)
                login(request, user)
                return redirect('home') 
            except Exception as e:
                return HttpResponse("Error: " + str(e))
        else:
            return HttpResponse("All fields are required")
    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  
            else:
                return HttpResponse("Invalid login")
        else:
            return HttpResponse("Username and password are required")
    return render(request, 'registration/login.html')
