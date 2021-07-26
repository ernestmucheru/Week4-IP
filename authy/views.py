from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.views import home
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user= form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context = {'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
       return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def profile(request, username):
    return render(request, 'profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})
