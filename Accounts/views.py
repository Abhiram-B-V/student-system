from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
def signup(request):
    if(request.method=='POST'):
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(request.POST['email'])
        if(User.objects.filter(email=email).exists()):
            messages.error(request,'User or Email already exist')
            return redirect(reverse('signup_url'))
        User.objects.create_user(username=username,email=email,password=password1)
        return redirect(reverse('login_url'))
    return render(request,'signup.html')


def login(request):
    if(request.method=='POST'):
        form=AuthenticationForm(data=request.POST)
        if(form.is_valid()):
            user=form.get_user()
            login_user(request,user)
            print("login successful")
            return redirect(reverse('home_url'))
        print("invalid login attempt")
    return render(request,'Home.html')