from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def register_view(request, *args, **kwargs):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. ")
            return redirect("home")
        
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="authUser/register.html", context={"register_form":form})

def login_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request=request, template_name="authUser/login.html", context={"login_form": form})

def logout_view(request, *args, **kwargs):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")