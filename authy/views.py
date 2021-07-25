from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main.views import home

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

def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, 'Your details have been updated')
            return redirect('profile')
    else:
         u_form = UserUpdateForm(instance = request.user)
         p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile.html',context)

