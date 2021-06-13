from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#TODO adding multiple user types from decorators and models
#from .decorators import user_required, employee_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Now you can log in {username}!')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
#@user_required
def logged_user(request):
    return render(request, 'users/logged_user.html')


@login_required()
#@employee_required
def logged_employee(request):
    return render(request, 'users/logged_employee.html')


@login_required()
#@employee_required
def orders(request):
    return render(request, 'users/orders.html')

