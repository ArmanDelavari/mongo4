from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationsForm

# Create your views here.
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login is successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'username or password is wrong', 'alert')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)



def user_logout(request):
    logout(request)
    messages.success(request, 'logout is successfully', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, 'your register successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationsForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)