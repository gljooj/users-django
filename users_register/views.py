from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.


def users_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users_register/users_list.html', context)


def user_edit(request, id):
    user = User.objects.filter(id=id).first()
    form = UserForm(instance=user)

    if request.method == 'POST':
        edit = UserForm(request.POST, instance=user)
        if edit.is_valid():
            edit.save()
            return redirect('/')

    context = {'form': form, 'user': user}
    return render(request, 'users_register/user.html', context)


def user_new(request):
    form = UserForm()

    if request.method == 'POST':
        edit = UserForm(request.POST)
        if edit.is_valid():
            edit.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'users_register/user_new.html', context)


def user_delete(request, id):
    user = User.objects.filter(id=id).first()

    if request.method == 'POST':
        user.delete()
        return redirect('/')
    context = {'user': user}
    return render(request, 'users_register/user_delete.html', context)
