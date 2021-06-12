from django.shortcuts import render


def home(request):
    return render(request, 'pizzeria/home.html')


def about(request):
    return render(request, 'pizzeria/about.html', {'title': 'O nas'})


def operator(request):
    return render(request, 'pizzeria/operator.html')
