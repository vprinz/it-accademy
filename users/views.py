from django.shortcuts import render


def login(request):
    context = {'title': 'Store - Авторизация'}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {'title': 'Store - Регистрация'}
    return render(request, 'users/registration.html', context)
